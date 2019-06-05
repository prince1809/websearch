from optparse import OptionParser, OptionGroup

from lib.utils.DefaultConfigParser import DefaultConfigParser
from lib.utils.FileUtils import File
from lib.utils.FileUtils import FileUtils


class ArgumentParser(object):
    def __init__(self, script_path):
        self.script_path = script_path
        self.parseConfig()

        options = self.parseArguments()

        if options.url == None:
            if options.urlList != None:
                with File(options.urlList) as urlList:
                    if not urlList.exists():
                        print("The file with URLs does not exist")
                        exit(0)

    def parseConfig(self):
        config = DefaultConfigParser()

    def parseArguments(self):
        usage = 'Usage'
        parser = OptionParser(usage)
        # Mandatory arguments
        mandatory = OptionGroup(parser, 'Mandatory')
        mandatory.add_option('-u', '--url', help='URL target', action='store', dest='url', default=None)
        mandatory.add_option('-L', '--url-list', help='URL list target', action='store', type='string', dest='urlList',
                             default=None)

        parser.add_option_group(mandatory)
        options, arguments = parser.parse_args()
        return options
