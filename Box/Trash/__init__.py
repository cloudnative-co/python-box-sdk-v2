from ..base import Base
from .folders import Folders


class Client(Base):
    __folders: Folders = None

    @property
    def folders(self):
        if self.__folders is None:
            self.__folders = Folders(client=self)
        return self.__folders
