# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments


class DevicePinners(Base):

    path = {
        "items": "enterprises/{enterprise_id}/device_pinners",
        "info": "device_pinners/{device_pinner_id}",
        "delete": "device_pinners/{device_pinner_id}"
    }

    def items(
        self, enterprise_id: str = None,
        direction: str = None, limit: int = None, marker: str = None
    ):
        args = locals()
        query = get_arguments(args)
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="get", path=path, query=query)

    def info(self, device_pinner_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path, query=query)

    def delete(self, device_pinner_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
