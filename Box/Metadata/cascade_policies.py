# -*- coding: utf-8 -*-
# import module snippets
import sys
from ..base import Base
from ..Utilities.utilities import get_arguments
from ..Utilities.utilities import formation


class CascadePolicies(Base):

    path = {
        "items": "metadata_cascade_policies",
        "info": "metadata_cascade_policies//{metadata_cascade_policy_id}",
        "create": "metadata_cascade_policies",
        "enforcement": "metadata_cascade_policies//{metadata_cascade_policy_id}",
        "delete": "metadata_cascade_policies//{metadata_cascade_policy_id}"
    }

    def items(
        self, folder_id: str, marker: str = None, offset: int = None,
        owner_enterprise_id: str = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(locals())
        return self.request(method="get", path=path, query=query)

    def info(self, metadata_cascade_policies_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="get", path=path)

    @formation
    def create(
        self,
        folder_id: str, scope: str, template_key: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.request(method="post", path=path, payload=payload)

    @formation
    def enforcement(
        self, metadata_cascade_policies_id: str, conflict_resolution: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="post", path=path, payload=payload)

    def delete(self, metadata_cascade_policies_id: str):
        path = self.path[sys._getframe().f_code.co_name].format(**locals())
        return self.request(method="delete", path=path)
