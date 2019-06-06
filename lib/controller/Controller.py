import os

from lib.utils import FileUtils


class SkipTargetInterrupt(Exception):
    pass


MAJOR_VERSION = 0
MINOR_VERSION = 3
REVISION = 8
VERSION = {
    "MAJOR_VERSION": MAJOR_VERSION,
    "MINOR_VERSION": MINOR_VERSION,
    "REVISION": REVISION
}


class Controller(object):
    def __init__(self, script_path, arguments, output):
        global VERSION
        program_banner = open(FileUtils.buildPath(script_path, "lib", "controller", "banner.txt")).read().format(
            **VERSION)

        self.script_path = script_path
        self.exit = False
        self.arguments = arguments
        self.output = output
        self.savePath = self.script_path
        self.doneDirs = []

        # self.recursive_level_max = self.arguments.recursive_level_max
