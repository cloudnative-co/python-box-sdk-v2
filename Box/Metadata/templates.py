# -*- coding: utf-8 -*-
# import module snippets
import sys
from ..base import Base
from ..Utilities.utilities import get_arguments
from ..Utilities.utilities import formation


class Templates(Base):

    path = {
        "items": "metadata_templates/{scope}",
        "info": "metadata_templates",
        "info_from_name": "metadata_templates/{scope}/{template_key}",
        "create": "metadata_templates/schema",
        "update": "metadata_templates/{scope}/{template_key}",
        "delete": "metadata_templates/{scope}/{template_key}"
    }

    def items(self, scope: str = None, limit: int = None, marker: str = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["limit", "marker"])
        return self.request(method="get", path=path, query=query)

    def info(self, metadata_instance_id: str = None):
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(args)
        return self.request(method="get", path=path, query=query)

    def info_from_name(self, metadata_instance_id: str = None):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    @formation
    def create(
        self,
        copy_instance_on_item_copy: bool = None,  display_name: str = None,
        fields: list = None, hidden: bool = None, scope: str = None,
        template_key: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="post", path=path, payload=payload)

    @formation
    def update(
        self, scope: str, template_key: str, item: list,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="put", path=path, payload=payload)

    def delete(self, scope: str, template_key: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
