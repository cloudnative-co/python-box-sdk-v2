# -*- coding: utf-8 -*-
# import module snippets
import sys
from ..base import Base
from ..Utilities.utilities import get_arguments


class Folders(Base):

    path = {
        "items": "folders/trash/items"
    }

    def items(
        self,
        direction: str = None, fields: list = None, limit: int = None,
        marker: str = None, offset: int = None, sort: str = None,
        usemarker: bool = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="get", path=path, query=query)
