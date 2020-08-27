
# -*- coding: utf-8 -*-
# import module snippets
import datetime
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Folders(Base):

    path = {
        "info": "folders/{folder_id}",
        "items": "folders/{folder_id}/items",
        "create": "folders",
        "copy": "folders/{folder_id}/copy",
        "update": "folders/{folder_id}",
        "delete": "folders/{folder_id}",
        "collaborations": "folders/{folder_id}/collaborations",
        "trash": "folders/{folder_id}/trash"
    }

    def info(self, folder_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    def items(
        self,
        folder_id: str,
        fields: list = None,
        usemarker: bool = None,
        marker: str = None,
        offset: int = None,
        sort: str = None,
        direction: str = None,
        limit: int = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, ignores=["folder_id"])
        return self.request(method="get", path=path, query=query)

    @formation
    def create(
        self,
        name: str,
        parent_id: str,
        folder_upload_email_access: str = None,
        sync_state: str = None,
        fields: list = None,
        payload: dict = None,
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )

    @formation
    def copy(
        self,
        folder_id: str,
        parent_id: str,
        name: str = None,
        fields: list = None,
        payload: dict = None,
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )

    @formation
    def update(
        self,
        folder_id: str,
        fields: list = None,
        can_non_owners_invite: bool = None,
        can_non_owners_view_collaborators: bool = None,
        collections_id: list = None,
        description: str = None,
        folder_upload_email_access: str = None,
        is_collaboration_restricted_to_enterprise: bool = None,
        name: str = None,
        parent_id: str = None,
        shared_link_access: str = None,
        shared_link_password: str = None,
        shared_link_permissions_can_download: bool = None,
        shared_link_unshared_at: datetime.datetime = None,
        sync_state: str = None,
        tags: list = None,
        if_match: str = None,
        payload: dict = None,
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        headers = get_arguments(args, keys=["if_match"])
        return self.request(
            method="put", path=path, query=query,
            payload=payload, headers=headers
        )

    def delete(
        self, folder_id: str, recursive: bool = None, if_match: str = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["recursive"])
        headers = get_arguments(args, keys=["if_match"])
        return self.request(
            method="delete", path=path, query=query, headers=headers
        )

    def collaborations(self, folder_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, ignores=["folder_id"])
        return self.request(method="get", path=path, query=query)

    def trash(self, folder_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(method="get", path=path, query=query)

    @formation
    def restore(
        self, folder_id: str, fields: list = None,
        name: str = None, parent_id: str = None, payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="post", path=path, query=query, payload=payload
        )

    def permanently_delete(self, folder_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
