# -*- coding: utf-8 -*-
# import module snippets
from .base import Base
from .collaborations import Collaborations
from .collections import Collections
from .comments import Comments
from .device_pinners import DevicePinners
from .events import Events
from .files import Files
from .folders import Folders
from .groups import Groups
from .invites import Invites
from .search import Search
from .tasks import Tasks
from .users import Users
from .versions import Versions
from .upload_sessions import UploadSessions
from .webhooks import Webhooks
from .Utilities import Uploader, Downloader
from .Metadata import Files as MetadataFiles
from .Metadata import Folders as MetadataFolders
from .Metadata import Templates as MetadataTemplates
from .Metadata import CascadePolicies
from .Trash import Folders as TrashFolders


class Client(Base):
    class Metadata(Base):
        @property
        def files(self):
            return MetadataFiles(client=self)

        @property
        def folders(self):
            return MetadataFolders(client=self)

        @property
        def templates(self):
            return MetadataTemplates(client=self)

        @property
        def cascade_policy(self):
            return CascadePolicies(client=self)

    class Trash(Base):
        @property
        def folders(self):
            return TrashFolders(client=self)

    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        enterprise_id: str = None,
        jwt_key_id: str = None,
        rsa_private_key_data: str = None,
        rsa_private_key_file_sys_path: str = None,
        rsa_private_key_passphrase: str = None,
        user_id: str = None,
        client: object = None,
        access_token: str = None
    ):
        super(Client, self).__init__(
            client_id,
            client_secret,
            enterprise_id,
            jwt_key_id,
            rsa_private_key_data,
            rsa_private_key_file_sys_path,
            rsa_private_key_passphrase,
            user_id,
            client,
            access_token
        )

    @property
    def collaborations(self):
        return Collaborations(client=self)

    @property
    def collections(self):
        return Collections(client=self)

    @property
    def comments(self):
        return Comments(client=self)

    @property
    def device_pinners(self):
        return DevicePinners(client=self)

    @property
    def events(self):
        return Events(client=self)

    @property
    def files(self):
        return Files(client=self)

    @property
    def folders(self):
        return Folders(client=self)

    @property
    def groups(self):
        return Groups(client=self)

    @property
    def invites(self):
        return Invites(client=self)

    @property
    def search(self):
        return Search(client=self)

    @property
    def tasks(self):
        return Tasks(client=self)

    @property
    def trush(self):
        return Trush(client=self)

    @property
    def users(self):
        return Users(client=self)

    @property
    def versions(self):
        return Versions(client=self)

    @property
    def upload_sessions(self):
        return UploadSessions(client=self)

    @property
    def webhooks(self):
        return Webhooks(client=self)

    @property
    def metadata(self):
        return Webhooks(client=self)

    @property
    def uploader(self):
        return Uploader(client=self)

    @property
    def downloader(self):
        return Downloader(client=self)

    @property
    def metadata(self):
        return self.__class__.Metadata(client=self)

    @property
    def trash(self):
        return self.__class__.Trash(client=self)
