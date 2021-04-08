# -*- coding: utf-8 -*-
# import module snippets
import json
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Search(Base):
    path = {
        "query": "search/",
    }

    def query(
        self,
        type: str = None,
        ancestor_folder_ids: list = None,
        content_types: list = None,
        created_at_range: list = None,
        direction: str = "DESC",
        fields: list = None,
        file_extensions: list = None,
        include_recent_shared_links: bool = None,
        limit: int = None,
        offset: int = None,
        owner_user_ids: list = None,
        query: str = None,
        scope: str = None,
        size_range: list = None,
        sort: str = None,
        trash_content: str = None,
        updated_at_range: str = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name]
        q = get_arguments(args)
        return self.request(method="get", path=path, query=q)
