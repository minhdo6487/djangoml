# -*- coding: utf-8 -*-
########################################################################
#
#    Config <<Singleton>>
#
########################################################################

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division

import os, sys
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lib"))
if path not in sys.path:
    sys.path.append(path)

from Singleton import Singleton
from ConfigParser import SafeConfigParser

class Config(Singleton):
    def singleton_init(self, config="config.ini"):
        config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "conf", config))
        self.parser = SafeConfigParser()
        self.parser.read(config_path)
        return

    def get(self, section, option):
        return self.parser.get(section, option)

    def getint(self, section, option):
        return self.parser.getint(section, option)

    def getboolean(self, section, option):
        return self.parser.getboolean(section, option)

    def sections(self):
        return self.parser.sections()

    def options(self, section):
        return self.parser.options(section)

# if __name__ == '__main__':
#     # test code
#     for section in Config().sections():
#         print "[%s]" % section
#         for option in Config().options(section):
#             print "%s: %s, %s" % (option, Config().get(section, option), type(Config().get(section, option)))
