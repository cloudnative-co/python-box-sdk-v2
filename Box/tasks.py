# -*- coding: utf-8 -*-
# import module snippets
import sys
import datetime
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Tasks(Base):

    path = {
        "items": "files/{file_id}/tasks",
        "info": "tasks/{task_id}",
        "create": "tasks",
        "update": "tasks/{task_id}",
        "delete": "tasks/{task_id}"
    }

    def items(self, file_id: str):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        return self.request(method="get", path=path)

    def info(self, task_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    @formation
    def create(
        self, action: str = None, completion_rule: str = None,
        due_at: datetime.datetime = None, item_id: str = None,
        item_type: str = None, message: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="post", path=path, payload=payload)

    @formation
    def update(
        self, task_id: str, action: str = None, completion_rule: str = None,
        due_at: datetime.datetime = None, message: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="put", path=path, payload=payload)

    def delete(self, task_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
