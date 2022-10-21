from ..base import Base
from .files import Files
from .folders import Folders
from .templates import Templates
from .cascade_policies import CascadePolicies


class Client(Base):
    __files: Files = None
    __folders: Folders = None
    __templates: Templates = None
    __cascade_policies: CascadePolicies = None

    @property
    def files(self):
        if self.__files is None:
            self.__files = Files(client=self)
        return self.__files

    @property
    def folders(self):
        if self.__folders is None:
            self.__folders = Folders(client=self)
        return self.__folders

    @property
    def templates(self):
        if self.__templates is None:
            self.__templates = Templates(client=self)
        return self.__templates

    @property
    def cascade_policies(self):
        if self.__cascade_policies is None:
            self.__cascade_policies = CascadePolicies(client=self)
        return self.__cascade_policies
