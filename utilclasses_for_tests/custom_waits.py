from pathlib import Path


class FileIsDownload(object):

    def __init__(self, path):
        self.path = path

    def __call__(self, *args):
        if Path(self.path).is_file():
            return True
        else:
            return False
