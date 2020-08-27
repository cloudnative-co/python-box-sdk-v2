# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Invites(Base):

    path = {
        "info": "invites/{invite_id}",
        "create": "invites",
    }

    def info(self, invite_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(method="get", path=path, query=query)

    @formation
    def create(
        self, fields: list = None,
        actionable_by_login: str = None,
        enterprise_id: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(locals(), keys=["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )
