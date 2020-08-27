# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments


class Collections(Base):

    path = {
        "items": "collections",
        "info": "collections/{collection_id}/items"
    }

    def items(
        self, fields: list = None, limit: int = None, offset: int = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="get", path=path, query=query)

    def info(
        self, collection_id: str,
        fields: list = None, limit: int = None, offset: int = None
    ):
        args = locals()
        query = get_arguments(args, ignores=["collection_id"])
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="get", path=path, query=query)
