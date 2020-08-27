# -*- coding: utf-8 -*-
# import module snippets
import sys
from ..Utilities.utilities import get_arguments
from ..base import Base


class Folders(Base):

    path = {
        "items": "folders/{folder_id}/metadata",
        "info": "folders/{folder_id}/metadata/{scope}/{template_key}",
        "create": "folders/{folder_id}/metadata/{scope}/{template_key}",
        "update": "folders/{folder_id}/metadata/{scope}/{template_key}",
        "delete": "folders/{folder_id}/metadata/{scope}/{template_key}"
    }

    def items(self, folder_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    def info(self, folder_id: str, scope: str, template: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    def create(self, folder_id: str, scope: str, template: str, payload: dict):
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="post", path=path, payload=payload)

    def update(folder_id: str, scope: str, template: str, payload: list):
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="put", path=path, payload=payload)

    def delete(self, folder_id: str, scope: str, template: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
