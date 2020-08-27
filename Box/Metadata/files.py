# -*- coding: utf-8 -*-
# import module snippets
import sys
from ..Utilities.utilities import get_arguments
from ..base import Base


class Files(Base):

    path = {
        "items": "files/{file_id}/metadata",
        "info": "files/{file_id}/metadata/{scope}/{template_key}",
        "create": "files/{file_id}/metadata/{scope}/{template_key}",
        "update": "files/{file_id}/metadata/{scope}/{template_key}",
        "delete": "files/{file_id}/metadata/{scope}/{template_key}"
    }

    def items(self, file_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    def info(self, file_id: str, scope: str, template: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    def create(self, file_id: str, scope: str, template: str, payload: dict):
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="post", path=path, payload=payload)

    def update(file_id: str, scope: str, template: str, payload: list):
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="put", path=path, payload=payload)

    def delete(self, file_id: str, scope: str, template: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
