# -*- coding: utf-8 -*-
# import module snippets
import sys
import datetime
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class CollaborationWhitelist(Base):

    path = {
        "items": "collaboration_whitelist_entries",
        "info": "collaboration_whitelist_entries/{collaboration_whitelist_entry_id}",
        "create": "collaboration_whitelist_entries",
        "update": "collaborations/{collaboration_id}",
        "delete": "collaboration_whitelist_entries/{collaboration_whitelist_entry_id}"
    }

    def items(
        self, limit: int = None, marker: str = None, usermaker: bool= None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="get", path=path, query=query)

    def info(self, collaboration_whitelist_entry_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    @formation
    def create(
        self, direction: str, domain: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(
            method="post", path=path, payload=payload
        )

    def delete(self, collaboration_whitelist_entry_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
