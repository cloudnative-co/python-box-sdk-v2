# -*- coding: utf-8 -*-
# import module snippets
import base64
import cryptography
import cryptography.hazmat.primitives.serialization
import datetime
import io
import json
import mimetypes
import os
import random
import string
import sys
import urllib.request

from .exception import APIException


class Base(object):
    headers: dict = {}
    auth_url: str = "https://api.box.com/oauth2/token"
    expire_time: datetime.datetime = None
    schema = "https"
    host = "api.box.com"
    version = "2.0"
    client_id: str = None
    client_secret: str = None
    key: str = None
    jwt_key_id: str = None
    access_token = None

    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        enterprise_id: str = None,
        jwt_key_id: str = None,
        rsa_private_key_data: str = None,
        rsa_private_key_file_sys_path: str = None,
        rsa_private_key_passphrase: str = None,
        user_id: str = None,
        client: object = None,
        access_token: str = None
    ):
        if client is not None:
            self.headers = client.headers
            self.expire_time = client.expire_time
            self.client_id = client.client_id
            self.client_secret = client.client_secret
            self.jwt_key_id = client.jwt_key_id
            self.key = client.key
        elif access_token is None:
            key = self.load_private_key(
                rsa_private_key_data,
                rsa_private_key_file_sys_path,
                rsa_private_key_passphrase
            )
            self.key = key
            self.jwt_key_id = jwt_key_id
            self.auth_request(
                client_id, client_secret, enterprise_id,
                jwt_key_id, key, user_id
            )
        else:
            auth = f"Bearer {access_token}"
            self.headers["Authorization"] = auth
            if user_id:
                self.headers["As-User"] = user_id


    def load_private_key(
        self,
        data: str = None, file_sys_path: str = None, passphrase: str = None
    ):
        if file_sys_path is not None:
            with open(file_sys_path, 'rb') as key_file:
                data = key_file.read()
                if hasattr(data, 'read') and callable(data.read):
                    data = data.read()
        data = data.encode('ascii')
        k = cryptography.hazmat.primitives.serialization.load_pem_private_key(
            data,
            password=passphrase,
            backend=cryptography.hazmat.backends.default_backend()
        )
        return k

    def create_claims(
        self, client_id, sub: str,
        sub_type: str = "enterprise", expire: int = 30
    ):
        now = datetime.datetime.utcnow()
        delta30 = now + datetime.timedelta(seconds=expire)
        exp = int(
            (delta30 - datetime.datetime(1970, 1, 1)).total_seconds()
        )
        rnd = random.SystemRandom()
        jti_len = rnd.randint(16, 128)
        asc_alpha = string.ascii_letters + string.digits
        asc_len = len(asc_alpha)
        jti = ''.join(
            asc_alpha[int(rnd.random() * asc_len)] for _ in range(jti_len)
        )
        payload = {
            'iss': client_id,
            'sub': sub,
            'box_sub_type': sub_type,
            'aud': self.auth_url,
            'jti': jti,
            'exp': exp
        }
        payload = json.dumps(payload, separators=(",", ":")).encode('utf-8')
        return base64.urlsafe_b64encode(payload).replace(b"=", b"")

    def create_jwt_header(self, public_key_id, algorithm="RS512"):
        header = {
            "typ": "JWT",
            "kid": public_key_id,
            "alg": algorithm
        }
        json_header = json.dumps(header, separators=(",", ":")).encode('utf-8')
        return base64.urlsafe_b64encode(json_header).replace(b"=", b"")

    def create_assertion(self, header, claims, key):
        segments = []
        segments.append(header)
        segments.append(claims)
        signature = key.sign(
            b".".join(segments),
            cryptography.hazmat.primitives.asymmetric.padding.PKCS1v15(),
            cryptography.hazmat.primitives.hashes.SHA512()
        )
        segments.append(base64.urlsafe_b64encode(signature).replace(b"=", b""))
        assertion = b'.'.join(segments)
        return assertion

    def auth_request(
        self, client_id: str = None, client_secret: str = None,
        enterprise_id: str = None, public_key_id: str = None,
        private_key: str = None, user_id: str = None
    ):
        if enterprise_id is not None:
            claims = self.create_claims(client_id, enterprise_id)
        elif user_id is not None:
            claims = self.create_claims(client_id, user_id, sub_type="user")

        header = self.create_jwt_header(public_key_id)
        assertion = self.create_assertion(header, claims, private_key)
        payload = {
            'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
            'assertion': assertion,
            "client_id": client_id,
            'client_secret': client_secret
        }
        now = datetime.datetime.utcnow()
        data = self.request(
            method="POST", path="oauth2/token", payload=payload, headers={}
        )
        self.expire_time = now + datetime.timedelta(seconds=data["expires_in"])
        self.access_token = data["access_token"]
        auth = "Bearer {access_token}".format(**data)
        if "As-User" in self.headers:
            del self.headers["As-User"]
        self.headers["Authorization"] = auth
        self.client_id = client_id
        self.client_secret = client_secret

    def revoke(self):
        if self.client_id is None or self.client_secret is None:
            return
        if "Authorization" not in self.headers:
            return
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "token": self.headers["Authorization"].replace("Bearer ", "")
        }
        del self.headers["Authorization"]
        if "As-User" in self.headers:
            del self.headers["As-User"]
        self.request(method="POST", path="oauth2/revoke", payload=payload)
        self.client_id = None
        self.client_secret = None

    def encode_multipart(
        self, payload: dict = None, files: dict = None, charset="utf-8"
    ):
        boundary = '----------lImIt_of_THE_fwIle_eW_$'
        bf = io.BytesIO()
        if payload is not None:
            for key, value in payload.items():
                bf.write(('--%s\r\n' % boundary).encode(charset))
                bf.write((
                    'Content-Disposition: form-data; name="%s"' % key
                ).encode(charset))
                bf.write(b'\r\n\r\n')
                if isinstance(value, dict):
                    value = json.dumps(value)
                if isinstance(value, str):
                    value = value.encode(charset)
                bf.write(value)
                bf.write(b'\r\n')
        if files is not None:
            cdisp = 'Content-Disposition: form-data; '\
                    'name="%s"; filename="%s"\r\n'
            for key, value in files.items():
                filename = value["name"]
                bf.write(('--%s\r\n' % boundary).encode(charset))
                bf.write((cdisp % (key, filename)).encode(charset))
                type = mimetypes.guess_type(filename)[0]
                type = type or 'application/octet-stream'
                bf.write(("Content-Type: {}\r\n".format(type)).encode(charset))
                content = value["content"]
                if hasattr(content, "read"):
                    content = content.read()
                bf.write(b'\r\n')
                bf.write(content)
                bf.write(b'\r\n')
        bf.write(('--' + boundary + '--\r\n\r\n').encode(charset))
        bf = bf.getvalue()
        content_type = 'multipart/form-data; boundary=%s' % boundary
        return content_type, bf

    def request(
        self,
        method: str, path: str = None, headers: dict = {},
        query: dict = None, payload: dict = None, url: str = None,
        files: dict = None, is_read: bool = True, with_header: bool = False,
        charset: str = "utf-8"
    ):
        if url is None:
            if path == "oauth2/token" or path == "oauth2/revoke":
                url = "{}://{}/{}".format(self.schema, self.host, path)
            else:
                url = "{}://{}/{}/{}".format(
                    self.schema, self.host, self.version, path
                )
        if "?" in url:
            q = url.split("?")
            if query is None:
                query = dict()
            for q1 in q[1].split("&"):
                q1 = q1.split("=")
                query[q1[0]] = q1[1]
        if not ((query is None) or (len(query) == 0)):
            url = "{}?{}".format(url, urllib.parse.urlencode(query))

        args = {
            "url": url,
            "method": method.upper()
        }
        ctype = headers.get('Content-Type', None)
        if ctype == "multipart/form-data":
            ctype, payload = self.encode_multipart(payload, files, charset)
            headers["Content-Type"] = ctype
            args["data"] = payload
        elif ctype == "application/octet-stream":
            args["data"] = payload
        elif payload is not None:
            try:
                payload = json.dumps(payload).encode('utf-8')
                headers["Content-Type"] = "application/json"
            except TypeError as e:
                try:
                    payload = urllib.parse.urlencode(payload).encode()
                except Exception as e:
                    pass
            args["data"] = payload
        else:
            payload = b""
        headers = dict(self.headers, **headers)
        args["headers"] = headers
        req = urllib.request.Request(**args)
        try:
            with urllib.request.urlopen(req) as res:
                head = dict(res.info())
                if is_read:
                    body = res.read()
                    try:
                        body = body.decode("utf-8")
                    except UnicodeDecodeError:
                        if with_header:
                            return body, head
                        return body
                    try:
                        body = json.loads(body)
                        if with_header:
                            return body, head
                        return body
                    except Exception as e:
                        if with_header:
                            return body, head
                        return body
                return res
        except urllib.error.HTTPError as e:
            raise APIException(e)

    def login(self, user: str):
        users = self.request(
            method="get", path="users", query={"filter_term": user}
        )
        if users["total_count"] == 0:
            raise Exception("User not found")
        user_id = users["entries"][0]["id"]
        self.auth_request(
            self.client_id,
            self.client_secret,
            None,
            self.jwt_key_id, self.key, user_id
        )
