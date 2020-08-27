# -*- coding: utf-8 -*-
# import module snippets
import json
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Users(Base):
    path = {
        "items": "users",
        "me": "users/me",
        "info": "users/{user_id}",
        "avatar": "users/{user_id}",
        "create": "users",
        "update": "users/{user_id}",
        "delete": "users/{user_id}",
        "memberships": "users/{user_id}/memberships"
    }

    def items(
        self,
        fields: list = None,
        filter_term: str = None,
        limit: int = None,
        marker: str = None,
        offset: int = None,
        usemarker: bool = None,
        user_type: str = None,
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(args)
        return self.request(method="get", path=path, query=query)

    def me(self):
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="get", path=path)

    def info(self, user_id: str, fields: list = None):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(method="get", path=path, query=query)

    def avatar(self, user_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    @formation
    def create(
        self,
        name: str,
        fields: list = None,
        address: str = None,
        can_see_managed_users: bool = None,
        external_app_user_id: str = None,
        is_exempt_from_device_limits: bool = None,
        is_exempt_from_login_verification: bool = None,
        is_external_collab_restricted: bool = None,
        is_platform_access_only: bool = None,
        is_sync_enabled: bool = None,
        job_title: str = None,
        language: str = None,
        login: str = None,
        phone: str = None,
        role: str = None,
        space_amount: int = None,
        status: str = None,
        timezone: str = None,
        tracking_codes: list = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(locals(), keys=["fields"])
        return self.request(
            method="post", path=self.path, query=query, payload=payload
        )

    def update(
        self,
        user_id: str,
        fields: list = None,
        address: str = None,
        can_see_managed_users: bool = None,
        enterprise: str = None,
        is_exempt_from_device_limits: bool = None,
        is_exempt_from_login_verification: bool = None,
        is_external_collab_restricted: bool = None,
        is_password_reset_required: bool = None,
        is_sync_enabled: bool = None,
        job_title: str = None,
        language: str = None,
        login: str = None,
        name: str = None,
        notification_email_email: str = None,
        notify: bool = None,
        phone: str = None,
        role: str = None,
        space_amount: int = None,
        status: str = None,
        timezone: str = None,
        tracking_codes: list = None,
        payload: dict = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["fields"])
        return self.request(
            method="put", path=path, query=query, payload=payload
        )

    def delete(
        self,
        user_id: str,
        force: bool = False,
        notify: bool = False
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args, keys=["force", "notify"])
        return self.request(method="delete", path=path, query=query)

    def memberships(
        self, user_id: str = None, limit: int = None, offset: int = None
    ):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name].format(**args)
        query = get_arguments(args)
        return self.request(method="get", path=self.path, query=query)
