# -*- coding: utf-8 -*-
# import module snippets
import sys
import datetime
import io
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Files(Base):
    path = {
        "info": "files/{file_id}",
        "thumbnail": "files/{file_id}/thumbnail.{extension}",
        "copy": "files/{file_id}/copy",
        "update": "files/{file_id}",
        "delete": "files/{file_id}",
        "content": "files/{file_id}/content",
        "preflight": "files/content",
        "upload": "https://upload.box.com/api/2.0/files/content",
        "collaborations": "files/{file_id}/collaborations",
        "trash": "files/{file_id}/trash",
        "restore": "files/{file_id}",
        "permanently_delete": "files/{file_id}/trash"
    }

    def info(
        self, file_id: str, fields: list = None, if_none_match: str = None,
        x_rep_hints: str = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        headers = get_arguments(args, keys=["if_none_match", "x_rep_hints"])
        return self.request(
            method="get", path=path, query=query, headers=headers
        )

    def thumbnail(
        self, file_id: str, extension: str,
        max_height: int = None, max_width: int = None,
        min_height: int = None, min_width: int = None,
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, ignores=[
            "max_height", "max_width", "min_height", "min_width"
        ])
        return self.request(method="get", path=path, query=query)

    @formation
    def copy(
        self,
        file_id: str,
        parent_id: str,
        name: str = None,
        version: str = None,
        fields: list = None,
        payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )

    @formation
    def update(
        self,
        file_id: str,
        description: str = None,
        lock_access: str = None,
        lock_expires_at: datetime.datetime = None,
        lock_is_download_prevented: bool = None,
        name: str = None,
        parent_id: str = None,
        permissions_can_download: str = None,
        shared_link_access: str = None,
        shared_link_password: str = None,
        shared_link_permissions_can_download: bool = None,
        shared_link_unshared_at: datetime.datetime = None,
        tags: list = None,
        fields: list = None,
        payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="put", path=path, query=query, payload=payload
        )

    def delete(self, file_id: str, if_match: str = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        headers = get_arguments(locals(), keys=["if_match"])
        return self.request(method="delete", path=path, headers=headers)

    def content(
        self, file_id: str, version: str = None, range: str = None,
        is_read: bool = True, with_header: bool = False
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["version"])
        headers = get_arguments(args, keys=["range"])
        return self.request(
            method="get", path=path, query=query,
            headers=headers, is_read=is_read, with_header=with_header
        )

    @formation
    def preflight(
        self, name: str = None, parent_id: str = None, size: int = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="options", path=path, payload=payload)

    @formation
    def upload(
        self,
        name: str,
        parent_id: str,
        file: io.BytesIO,
        fields: list = None,
        content_created_at: datetime.datetime = None,
        content_modified_at: datetime.datetime = None,
        content_md5: str = None,
        charset: str = "utf-8",
        payload: dict = None
    ):
        args = locals()
        url = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        headers = get_arguments(locals(), keys=["content_md5"])
        headers["Content-Type"] = "multipart/form-data"
        files = {
            "file": {
                "name": name,
                "content": file
            }
        }
        return self.request(
            method="post", query=query, url=url,
            headers=headers, payload=payload, files=files, charset=charset
        )

    def collaborations(
        self, file_id: str,
        fields: list = None, limit: int = None, marker: str = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, ignores=["file_id"])
        return self.request(method="get", path=path, query=query)

    def trash(self, file_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(method="get", path=path, query=query)

    @formation
    def restore(
        self, file_id: str, fields: list = None,
        name: str = None, parent_id: str = None, payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )

    def permanently_delete(self, file_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
