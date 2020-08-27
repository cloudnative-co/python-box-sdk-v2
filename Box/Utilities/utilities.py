import base64
import datetime
import dateutil.parser
import hashlib
import hmac
import inspect
import json
import pytz

from .maps import Maps


HEADER_KEYS = [
    "if_match",
    "if_none_match",
    "x_rep_hints",
    "content_md5",
    "content_range",
    "content_type",
    "content_length",
    "digest",
    "range"
]


def get_arguments(args: dict, keys: list = None, ignores: list = None):
    def snake_to_kebab(key):
        ret = []
        for key in key.split("_"):
            ret.append(key.capitalize())
        return "-".join(ret)

    ret = {}
    for ky in args:
        if ky == "self":
            continue
        if keys is not None:
            if ky not in keys:
                continue
        if ignores is not None:
            if ky in ignores:
                continue
        if args[ky] is None:
            continue
        if args[ky] is not None:
            if isinstance(args[ky], datetime.datetime):
                ret[ky] = args[ky].strftime("%Y-%m-%dT%H:%M:%S%z")
            elif isinstance(args[ky], list):
                ret[ky] = ",".join(args[ky])
            else:
                ret[ky] = args[ky]
        if ky in HEADER_KEYS:
            v = ret.pop(ky)
            ky = snake_to_kebab(ky)
            ret[ky] = v
    return ret


def validation(f):
    def wrapper(*args, **kwargs):
        method_name = f.__qualname__
        schema = Schemas[method_name]
        try:
            _kwargs = get_arguments(kwargs)
            validate(_kwargs, schema)
        except ValidationError as e:
            raise e
        return f(*args, **kwargs)
    return wrapper


def formation(f):
    def remove_none(params: dict):
        result = {}
        for k in params:
            v = params.get(k, None)
            if v is None:
                continue
            if isinstance(v, dict):
                v = remove_none(v)
                if v is None:
                    continue
            if isinstance(v, list):
                tmp_lst = []
                for v1 in v:
                    if isinstance(v1, dict):
                        v1 = remove_none(v1)
                        if v1 is None:
                            continue
                    tmp_lst.append(v1)
                if len(tmp_lst) == 0:
                    continue
                v = tmp_lst
            result[k] = v
        if len(result) == 0:
            return None
        return result

    def wrapper(*args, **kwargs):
        if "payload" in kwargs:
            return f(*args, **kwargs)
        m = inspect.getmembers(f)
        a, member = m[0]
        lst_args = list(member.keys())
        _kwargs = {}
        for arg_name in lst_args:
            arg_value = "null"
            if arg_name in kwargs:
                arg_value = kwargs.get(arg_name)
                if arg_value is None:
                    arg_value = "null"
                elif member[arg_name] == bool:
                    arg_value = "true" if arg_value else "false"
                elif member[arg_name] == str:
                    arg_value = '"{}"'.format(arg_value)
                elif member[arg_name] == datetime.datetime:
                    arg_value = arg_value.strftime("%Y-%m-%dT%H:%M:%S%z")
                    arg_value = '"{}"'.format(arg_value)
                elif member[arg_name] == list:
                    arg_value = json.dumps(arg_value)
            _kwargs[arg_name] = arg_value
        method_name = f.__qualname__
        maps = Maps[method_name]
        str_params = maps.format(**_kwargs)
        payload = json.loads(str_params)
        payload = remove_none(payload)
        kwargs["payload"] = payload
        return f(*args, **kwargs)
    return wrapper


def signature_validate(
    timestamp: str, primary_key: str, secondary_key: str,
    signature1: str, signature2: str, payload: str,
    debug: bool = False
):
    """
    args[in]    timestamp       box-delivery-timestampヘッダー
    args[in]    primary_key     プライマリーキー
    args[in]    secondary_key   セカンダリーキー
    args[in]    signature1      box-signature-primaryヘッダー
    args[in]    signature2      box-signature-secondaryヘッダー
    args[in]    payload         Webhookのbody
    return      bool, str       Validationの成否
    """

    if debug:
        return True, None
    date = dateutil.parser.parse(timestamp).astimezone(pytz.utc)
    now = datetime.datetime.now(pytz.utc)
    delta = datetime.timedelta(minutes=10)
    expiry_date = now - datetime.timedelta(minutes=10)

    expired = date >= expiry_date
    if not expired:
        return False, "Timestamp Invalid"

    byt = bytes(payload, 'utf-8') + bytes(timestamp, 'utf-8')

    hmac1 = hmac.new(str.encode(primary_key), byt, hashlib.sha256).digest()
    hmac2 = hmac.new(str.encode(secondary_key), byt, hashlib.sha256).digest()
    digest1 = base64.b64encode(hmac1).decode()
    digest2 = base64.b64encode(hmac2).decode()
    valid1 = digest1 == signature1
    valid2 = digest2 == signature2
    if not(valid1 and valid2):
        return False, "Signature Invalid"
    return True, "OK"


def webhook_response(body: str):
    """
    @brief      BoxWebhook用レスポンスの返却
    @params[in] イベントBODY
    """
    bd = json.loads(body)
    id = bd.get("id", None)
    source = bd.get("source", "{}")
    source_id = source.get("id", None)
    source_name = source.get("name", None)
    trigger = bd.get("trigger")
    result = 'webhook={}, trigger={}, source=<file id={} name="{}">'.format(
        id, trigger, source_id, source_name
    )
    return {
       "statusCode": 200,
       "body": result
    }
