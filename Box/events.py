# -*- coding: utf-8 -*-
# import module snippets
import datetime
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Events(Base):

    path = "events"

    def items(
        self,
        created_after: datetime.datetime = None,
        created_before: datetime.datetime = None,
        event_type: list = None,
        limit: int = None,
        stream_position: str = None,
        stream_type: str = None
    ):
        query = get_arguments(locals())
        return self.request(method="get", path=self.path, query=query)

    def endpoint(self):
        return self.request(method="options", path=self.path)
