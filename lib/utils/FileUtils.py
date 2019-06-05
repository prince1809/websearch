import os


class File(object):
    def __init__(self, *pathComponents):
        self.path = FileUtils.buildPath(*pathComponents)
        self.content = None


class FileUtils(object):
    @staticmethod
    def buildPath(*pathComponents):
        if pathComponents:
            path = os.path.join(*pathComponents)
        else:
            path = ''
        return path
