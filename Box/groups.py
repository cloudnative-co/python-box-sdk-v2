# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Groups(Base):

    path = {
        "items": "groups",
        "info": "groups/{group_id}",
        "create": "groups",
        "update": "groups/{group_id}",
        "delete": "groups/{group_id}",
        "collaborations": "groups/{group_id}/collaborations",
        "memberships": "groups/{group_id}/memberships"
    }

    def items(
        self, fields: list = None, limit: int = None, offset: int = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="get", path=path, query=query)

    def info(self, group_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(method="get", path=path, query=query)

    @formation
    def create(
        self, name: str, fields: list = None, description: str = None,
        external_sync_identifier: str = None, invitability_level: str = None,
        member_viewability_level: str = None, provenance: str = None,
        payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )

    @formation
    def update(
        self, group_id: str = None, fields: list = None,
        description: str = None, external_sync_identifier: str = None,
        invitability_level: str = None, member_viewability_level: str = None,
        name: str = None, provenance: str = None, payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="put", path=path, query=query, payload=payload
        )

    def delete(self, group_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)

    def collaborations(
        self, group_id: str, limit: int = None, offset: int = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, ignores=["group_id"])
        return self.request(method="get", path=path, query=query)

    def memberships(
        self, group_id: str = None, limit: int = None, offset: int = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args)
        return self.request(method="get", path=self.path, query=query)
