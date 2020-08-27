# -*- coding: utf-8 -*-
# import module snippets
import json
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class GroupMemberships(Base):
    path = {
        "info": "group_memberships/{group_membership_id}",
        "add": "group_memberships",
        "update": "group_memberships/{group_membership_id}",
        "remove": "group_memberships/{group_membership_id}",
    }

    def info(self, group_membership_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(method="get", path=path, query=query)

    @formation
    def add(
        self,
        fields: list = None,
        configurable_permissions: list = None, group_id: str = None,
        role: str = None, user_id: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(locals(), keys=["fields"])
        return self.request(
            method="post", path=self.path, query=query, payload=payload
        )

    def update(
        self, group_membership_id: str, fields: list = None,
        configurable_permissions: list = None, role: str = None,
        payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="put", path=path, query=query, payload=payload
        )

    def remove(self, group_membership_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
