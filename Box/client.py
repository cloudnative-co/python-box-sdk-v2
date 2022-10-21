# -*- coding: utf-8 -*-
# import module snippets
from .base import Base
from .collaborations import Collaborations
from .collections import Collections
from .collaboration_whitelist import CollaborationWhitelist
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
from .Metadata import Client as Metadata
from .Trash import Client as Trash


class Client(Base):

    __collaborations: Collaborations = None
    __collaboration_whitelist: CollaborationWhitelist = None
    __collections: Collections = None
    __comments: Comments = None
    __device_pinners: DevicePinners = None
    __events: Events = None
    __files: Files = None
    __folders: Folders = None
    __groups: Groups = None
    __invites: Invites = None
    __metadata: Metadata = None
    __search: Search = None
    __tasks: Tasks = None
    __trash: Trash = None
    __users: Users = None
    __versions: Versions = None
    __upload_sessions: UploadSessions = None
    __webhooks: Webhooks = None

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
        if self.__collaborations is None:
            self.__collaborations = Collaborations(client=self)
        return self.__collaborations

    @property
    def collaboration_whitelist(self):
        if self.__collaboration_whitelist is None:
            self.__collaboration_whitelist = CollaborationWhitelist(
                client=self
            )
        return self.__collaboration_whitelist

    @property
    def collections(self):
        if self.__collections is None:
            self.__collections = Collections(client=self)
        return self.__collections

    @property
    def comments(self):
        if self.__comments is None:
            self.__comments = Comments(client=self)
        return self.__comments

    @property
    def downloader(self):
        if self.__downloader is None:
            self.__downloader = Downloader(client=self)
        return self.__downloader

    @property
    def device_pinners(self):
        if self.__device_pinners is None:
            self.__device_pinners = DevicePinners(client=self)
        return self.__device_pinners

    @property
    def events(self):
        if self.__events is None:
            self.__events = Events(client=self)
        return self.__events

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
    def groups(self):
        if self.__groups is None:
            self.__groups = Groups(client=self)
        return self.__groups

    @property
    def invites(self):
        if self.__invites is None:
            self.__invites = Invites(client=self)
        return self.__invites

    @property
    def metadata(self):
        if self.__metadata is None:
            self.__metadata = Metadata(client=self)
        return self.__metadata

    @property
    def search(self):
        if self.__search is None:
            self.__search = Search(client=self)
        return self.__search

    @property
    def tasks(self):
        if self.__tasks is None:
            self.__tasks = Tasks(client=self)
        return self.__tasks

    @property
    def trash(self):
        if self.__trash is None:
            self.__trash = Trash(client=self)
        return self.__trash

    @property
    def users(self):
        if self.__users is None:
            self.__users = Users(client=self)
        return self.__users

    @property
    def versions(self):
        if self.__versions is None:
            self.__versions = Versions(client=self)
        return self.__versions

    @property
    def upload_sessions(self):
        if self.__upload_sessions is None:
            self.__upload_sessions = UploadSessions(client=self)
        return self.__upload_sessions

    @property
    def uploader(self):
        if self.__uploader is None:
            self.__uploader = Uploader(client=self)
        return self.__uploader

    @property
    def webhooks(self):
        if self.__webhooks is None:
            self.__webhooks = Webhooks(client=self)
        return self.__webhooks
