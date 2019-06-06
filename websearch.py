#!/usr/bin/env python3


from lib.core import ArgumentParser
from lib.controller import *
from lib.output import *

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, websearch requires Python 3.x\n")
    sys.exit(1)


class Program(object):
    def __init__(self):
        self.script_path = (os.path.dirname(os.path.realpath(__file__)))
        self.arguments = ArgumentParser(self.script_path)
        self.output = CLIOutput()
        self.controller = Controller(self.script_path, self.arguments, self.output)


if __name__ == '__main__':
    main = Program()
