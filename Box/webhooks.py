# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Webhooks(Base):

    path = {
        "items": "webhooks",
        "info": "webhooks/{webhook_id}",
        "create": "webhooks",
        "update": "webhooks/{webhook_id}",
        "delete": "webhooks/{webhook_id}"
    }

    def items(self, marker: str = None, limit: int = 100):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(args, keys=["limit", "marker"])
        return self.request(method="get", path=path, query=query)

    def info(self, webhook_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    @formation
    def create(
        self,
        address: str,
        triggers: list,
        target_id: str = None,
        target_type: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="post", path=path, payload=payload)

    @formation
    def update(
        self,
        webhook_id: str, address: str = None, triggers: list = None,
        target_id: str = None, target_type: str = None, payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="put", path=path, payload=payload)

    def delete(self, webhook_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="post", path=path)
