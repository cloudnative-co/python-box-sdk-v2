
# -*- coding: utf-8 -*-
# import module snippets
import sys
import datetime
import hashlib
import io
import re
import base64
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class UploadSessions(Base):

    path = {
        "info": "https://upload.box.com/api/2.0/files/upload_sessions/{upload_session_id}",
        "items": "https://upload.box.com/api/2.0/files/upload_sessions/{upload_session_id}/parts",
        "create": "https://upload.box.com/api/2.0/files/upload_sessions",
        "create_exists": "https://upload.box.com/api/2.0/files/{file_id}/upload_sessions",
        "commit": "https://upload.box.com/api/2.0/files/upload_sessions/{upload_session_id}/commit",
        "upload": "https://upload.box.com/api/2.0/files/upload_sessions/{upload_session_id}",
        "delete": "https://upload.box.com/api/2.0/files/upload_sessions/{upload_session_id}"
    }

    def info(self, upload_session_id: str):
        url = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", url=url)

    def items(
        self,
        upload_session_id: str,
        offset: int = None,
        limit: int = None
    ):
        args = locals()
        url = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, ignores=["upload_session_id"])
        return self.request(method="get", url=url, query=query)

    @formation
    def create(
        self,
        file_name: str,
        file_size: int,
        folder_id: str,
        payload: dict = None,
    ):
        url = self.path[sys._getframe().f_code.co_name]
        return self.request(method="post", url=url, payload=payload)

    @formation
    def create_exists(
        self,
        file_id: str,
        file_size: int,
        file_name: str = None,
        payload: dict = None,
    ):
        url = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="post", url=url, payload=payload)

    @formation
    def commit(
        self,
        upload_session_id: str,
        parts: list,
        sha1,
        if_match: str = None,
        if_none_match: str = None,
        payload: dict = None,
    ):
        content_sha1 = sha1.digest()
        content_sha1 = base64.b64encode(content_sha1).decode('utf-8')
        digest = 'SHA={0}'.format(content_sha1)
        args = locals()
        url = self.path[sys._getframe().f_code.co_name].format(**args)
        headers = get_arguments(
            args, keys=["digest", "if_none_match", "if_match"]
        )
        return self.request(
            method="post", url=url, payload=payload, headers=headers
        )

    def upload(
        self, upload_session_id: str, content_range: str,
        content: io.BytesIO
    ):
        regex = r"^bytes\s([0-9]+)-([0-9]+)\/[0-9]+$"
        matches = re.search(regex, content_range)
        if matches is None:
            return
        offset = int(matches.group(1))
        end = int(matches.group(2))
        content.seek(offset)
        size = end - offset
        size = size + 1
        buffer = content.read(size)
        sha1 = hashlib.sha1()
        sha1.update(buffer)
        content_sha1 = sha1.digest()
        content_sha1 = base64.b64encode(content_sha1).decode('utf-8')
        digest = 'SHA={0}'.format(content_sha1)
        args = locals()
        headers = get_arguments(args, keys=["digest", "content_range"])
        headers["Content-Type"] = "application/octet-stream"
        url = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(
            method="put", url=url, payload=buffer,
            headers=headers
        ), buffer

    def delete(self, upload_session_id: str):
        url = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", url=url)
