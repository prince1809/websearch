import threading
import sys
import platform


class CLIOutput(object):
    def __init__(self):
        self.lastLength = 0
        self.lastOutput = 0
        self.lastInline = False
        self.mutex = threading.Lock()
        self.blacklists = {}
        self.mutexCheckedPaths = threading.Lock()
        self.basePath = None
        self.errors = 0

    def inLine(self, string):
        self.erase()
        sys.stdout.write(string)
        sys.stdout.flush()
        self.lastInline = True

    def erase(self):
        if platform.system() == "Windows":
            csbi = GetConsoleScreenBufferInfo()
