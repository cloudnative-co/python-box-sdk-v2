# -*- coding: utf-8 -*-
# import module snippets
import sys
import datetime
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Collaborations(Base):

    path = {
        "items": "collaborations",
        "info": "collaborations/{collaboration_id}",
        "create": "collaborations",
        "update": "collaborations/{collaboration_id}",
        "delete": "collaborations/{collaboration_id}"
    }

    def items(
        self, fields: list = None, limit: int = None,
        offset: int = None, status: str = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(locals())
        return self.request(method="get", path=path, query=query)

    def info(self, collaboration_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(locals(), keys=["fields"])
        return self.request(method="get", path=path, query=query)

    @formation
    def create(
        self,
        fields: list = None, notify: bool = None,
        accessible_by_id: str = None, accessible_by_login: str = None,
        accessible_by_type: str = None, can_view_path: bool = None,
        item_id: str = None, item_type: str = None, role: str = None,
        payload: dict = None
    ):
        query = get_arguments(locals(), keys=["fields", "notify"])
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(
            method="post", path=path, payload=payload, query=query
        )

    @formation
    def update(
        self, collaboration_id: str,
        can_view_path: bool = None, expires_at: datetime.datetime = None,
        role: str = None, status: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="put", path=path, payload=payload)

    def delete(self, collaboration_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
