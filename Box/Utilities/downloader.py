# -*- coding: utf-8 -*-
# import module snippets
import concurrent.futures

from ..base import Base
from ..exception import APIException
from ..files import Files
from ..versions import Versions


class Downloader(Base):

    def download(
        self,
        file_id: str,
        version: str = None,
        chunk_size: int = 20000000,
        thread: bool = True
    ):
        files = Files(client=self)
        if version is None:
            info = files.info(file_id=file_id)
            file_size = info["size"]
        else:
            ver = Versions(client=self)
            info = ver.info(file_id=file_id, file_version_id=version)
            file_size = info["size"]
        if file_size > 20000000:
            total_parts, mod = divmod(file_size, chunk_size)
            if mod > 0:
                total_parts = total_parts + 1
            thread_pool = concurrent.futures.ThreadPoolExecutor(total_parts)
            futures = []
            temp = {}
            for offset in range(0, file_size, chunk_size):
                end_size = min(offset + chunk_size - 1, file_size - 1)
                str_range = "bytes={}-{}".format(offset, end_size)
                if thread:
                    th_args = {
                        "file_id": file_id,
                        "version": version,
                        "range": str_range,
                        "with_header": True
                    }
                    future = thread_pool.submit(
                         files.content, **th_args
                    )
                    futures.append(future)
                else:
                    body, head = files.content(
                        file_id=file_id, version=version,
                        range=str_range, with_header=True,
                    )
                    crange = head.get("Content-Range")
                    crange = int(crange.split("-")[0].replace("bytes ", ""))
                    temp[crange] = body
            if thread:
                for future in concurrent.futures.as_completed(futures):
                    body, head = future.result()
                    crange = head.get("Content-Range")
                    crange = int(crange.split("-")[0].replace("bytes ", ""))
                    temp[crange] = body
                thread_pool.shutdown()

            results = dict(sorted(temp.items(), key=lambda x: x[0]))
            ret = bytes()
            for key, value in results.items():
                ret = ret + value
            return ret
        else:
            return files.content(file_id=file_id)
