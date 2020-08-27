
# -*- coding: utf-8 -*-
# import module snippets
import sys
import io
import datetime
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Versions(Base):
    path = {
        "items": "files/{file_id}/versions",
        "info": "files/{file_id}/versions/{file_version_id}",
        "restoration": "files/{file_id}/versions/current",
        "upload": "https://upload.box.com/api/2.0/files/{file_id}/content",
        "delete": "files/{file_id}/versions/{file_version_id}"
    }

    def items(
        self, file_id: str, fields: list = None,
        limit: int = None, offset: int = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, ignores=["file_id"])
        return self.request(method="get", path=path, query=query)

    def info(self, file_id: str, file_version_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(method="get", path=path, query=query)

    @formation
    def restoration(
        self,
        file_id: str, fields: list = None,
        file_version_id: str = None, type: str = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )

    @formation
    def upload(
        self,
        file_id: str,
        file: io.BytesIO,
        fields: list = None,
        content_modified_at: datetime.datetime = None,
        content_md5: str = None,
        if_match: str = None,
        charset: str = "utf-8",
        payload: dict = None
    ):
        args = locals()
        url = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        headers = get_arguments(locals(), keys=["content_md5", "if_match"])
        headers["Content-Type"] = "multipart/form-data"
        files = {
            "file": {
                "name": "file",
                "content": file
            }
        }
        return self.request(
            method="post", query=query, url=url,
            headers=headers, payload=payload, files=files, charset=charset
        )

    def delete(self, file_id: str, file_version_id: str, if_match: str = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        headers = get_arguments(args, keys=["if_match"])
        return self.request(method="get", path=path, headers=headers)
