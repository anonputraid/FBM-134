#!/usr/bin/python3
# -*- Author : Anonputraid -*-    
#
# This user interface provides users with a command console interface to the
# Framework.
#

import argparse
from lib.core.api_common import metadata_base
from lib.core.api_common import clean
from lib.core.api_common import banner
from lib.core.api_common import version
from scripts import http_brute
from scripts import http_passwords

parser = argparse.ArgumentParser(description='FBM-134 Is A Brutal Attack Hacking Tool ')
parser.add_argument('-c', '--command', help='run in single command mode & execute provided command', action='store')
args = parser.parse_args()


commands = {
    'help':             metadata_base,
    'brutefb':          http_brute.interactive,
    'createword':       http_passwords.interactive,
    'version':          version,
    'clear':            clean,
    'banner':           banner,
    'exit':             quit
}


def console():
    from lib.core import api_printout as opt

    try:
        while True:
            if args.command:
                cmd = args.command
                intr = commands.get(args.command)
            else:
                opt.printout("~$ ", opt.YELLOW)
                cmd = input()
                intr = commands.get(cmd)

            if intr:
                intr()

        pass
    except KeyboardInterrupt:
        pass
    pass

if __name__ == "__main__":
    pass