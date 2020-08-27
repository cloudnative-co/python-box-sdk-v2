# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Comments(Base):

    path = {
        "items": "files/{file_id}/comments",
        "info": "comments/{comment_id}",
        "create": "comments",
        "update": "comments/{comment_id}",
    }

    def items(
        self, file_id: str,
        fields: list = None, limit: int = None, offset: int = None
    ):
        args = locals()
        query = get_arguments(args, ignores=["file_id"])
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="get", path=path, query=query)

    def info(self, comment_id: str, fields: list = None):
        args = locals()
        query = get_arguments(args, ignores=["comment_id"])
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="get", path=path, query=query)

    @formation
    def create(
        self,
        message: str, tagged_message: str,
        item_type: str = None, item_id: str = None,
        fields: list = None,
        payload: dict = None
    ):
        query = get_arguments(locals(), keys=["fields"])
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(
            method="post", path=path, payload=payload, query=query
        )

    @formation
    def update(
        self,
        comment_id: str,
        fields: list = None,
        message: str = None,
        payload: dict = None
    ):
        args = locals()
        query = get_arguments(args, keys=["fields"])
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(
            method="put", path=path, payload=payload, query=query
        )

    def delete(self, comment_id: str):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="delete", path=path)
