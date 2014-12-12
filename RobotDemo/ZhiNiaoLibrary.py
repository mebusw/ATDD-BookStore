import gzip
import os


class ZhiNiaoLibrary(object):
    """Test library for testing Zhiniao API.
    """

    def __init__(self):
        pass

    def ungzip_string(self, compressed):
        FILE_PATH = './~rf-request.gz'
        with open(FILE_PATH, 'wb+') as zf:
            zf.write(compressed)
        with gzip.open(FILE_PATH, 'rb+') as df:
            return df.read()

    def create_array(self, *ele):
        return map(lambda x: x, ele)

    def create_array_with_range(self, start, stop=None, step=1):
        if stop is None:
            return range(0, start, step)
        return range(start, stop, step)