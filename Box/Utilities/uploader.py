# -*- coding: utf-8 -*-
# import module snippets
import asyncio
import concurrent.futures
import datetime
import hashlib
import io

from ..base import Base
from ..exception import APIException
from ..files import Files
from ..upload_sessions import UploadSessions
from ..versions import Versions


class Uploader(Base):

    def upload(
        self,
        file_name: str,
        file_size: int,
        folder_id: str,
        content: io.BytesIO,
        fields: list = None,
        content_created_at: datetime.datetime = None,
        content_modified_at: datetime.datetime = None,
        overwrite: bool = True,
        threading: bool = False,
        is_asyncio: bool = False,
        charset: str = "utf-8"
    ):
        exists = False
        file_id = None
        file = Files(client=self)
        try:
            preflight = file.preflight(
                 name=file_name, parent_id=folder_id, size=file_size
            )
        except APIException as e:
            if e.state == 409:
                exists = True
                if not overwrite and exists:
                    raise e
                file_id = e.info["conflicts"]["id"]
            else:
                raise e
        if file_size <= 20000000:
            if exists:
                version = Versions(client=self)
                response = version.upload(
                    file_id=file_id,
                    file=content,
                    fields=fields,
                    content_modified_at=content_modified_at,
                    charset=charset
                )
            else:
                response = file.upload(
                    name=file_name,
                    parent_id=folder_id,
                    file=content,
                    fields=fields,
                    content_created_at=content_created_at,
                    content_modified_at=content_modified_at,
                    charset=charset
                )
        else:
            upload_session = UploadSessions(client=self)
            if exists:
                session = upload_session.create_exists(
                    file_name=file_name, file_size=file_size,
                    file_id=file_id
                )
            else:
                session = upload_session.create(
                    file_name=file_name, file_size=file_size,
                    folder_id=folder_id
                )
            upload_session_id = session["id"]
            total_size = file_size
            total_parts = session["total_parts"]
            part_size = session["part_size"]
            sha1 = hashlib.sha1()
            buffers = {}
            plist = []

            if threading:
                futures = []
                upload_range = range(0, total_size, part_size)
                workers = len(upload_range)
                with concurrent.futures.ThreadPoolExecutor(
                    max_workers=workers
                ) as executor:
                    for offset in range(0, total_size, part_size):
                        chunk_size = min(
                            offset + part_size - 1, total_size - 1
                        )
                        if chunk_size > total_size:
                            chunk_size = total_size
                        content_range = "bytes {}-{}/{}".format(
                            offset, chunk_size, total_size
                        )
                        args = [upload_session_id, content_range, content]
                        futures.append(
                            executor.submit(upload_session.upload, *args)
                        )
                    for future in futures:
                        resp, buffer = future.result(timeout=150)
                        buffers[resp["part"]["part_id"]] = buffer
                        plist.append(resp["part"])
            elif is_asyncio:
                loop = asyncio.get_event_loop()
                glist = list()
                for offset in range(0, total_size, part_size):
                    chunk_size = min(offset + part_size - 1, total_size - 1)
                    if chunk_size > total_size:
                        chunk_size = total_size
                    content_range = "bytes {}-{}/{}".format(
                        offset, chunk_size, total_size
                    )
                    glist.append(upload_session.upload(
                        upload_session_id, content_range, content
                    ))
                gather = asyncio.gather(*glist)
                results = loop.run_until_complete(gather)
                loop.close()
                for resp, buffer in results:
                    buffers[resp["part"]["part_id"]] = buffer
                    plist.append(resp["part"])
            else:
                parts_response = []
                for offset in range(0, total_size, part_size):
                    chunk_size = min(offset + part_size - 1, total_size - 1)
                    if chunk_size > total_size:
                        chunk_size = total_size
                    content_range = "bytes {}-{}/{}".format(
                        offset, chunk_size, total_size
                    )
                    parts_response.append(upload_session.upload(
                        upload_session_id, content_range, content
                    ))
                for resp, buffer in parts_response:
                    buffers[resp["part"]["part_id"]] = buffer
                    plist.append(resp["part"])

            new_plist = sorted(plist, key=lambda k: k['offset'])
            for resp in new_plist:
                buffer = buffers[resp["part_id"]]
                sha1.update(buffer)
            response = upload_session.commit(
                upload_session_id=upload_session_id,
                parts=new_plist,
                sha1=sha1
            )
        return response
