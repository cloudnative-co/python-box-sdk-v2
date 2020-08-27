# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class WebLinks(Base):

    path = {
        "info": "web_links/{web_link_id}",
        "create": "web_links",
        "update": "web_links/{web_link_id}",
        "delete": "web_links/{web_link_id}",
        "trash": "web_links/{web_link_id}/trash",
        "restore": "web_links/{web_link_id}",
        "permanently_delete": "web_links/{web_link_id}/trash"
    }

    def info(self, web_link_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    @formation
    def create(
        self, description: str = None, name: str = None, parent_id: str = None,
        url: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="post", path=path, payload=payload)

    @formation
    def update(
        self,
        web_link_id: str, description: str = None, name: str = None,
        parent_id: str = None, url: str = None, payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="put", path=path, payload=payload)

    def delete(self, web_link_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="post", path=path)

    def trash(self, web_link_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys["fields"])
        return self.request(method="get", path=path)

    @formation
    def restore(
        self, web_link_id: str,
        fields: list = None, name: str = None, parent_id: str = None,
        payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )

    def permanently_delete(self, web_link_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
