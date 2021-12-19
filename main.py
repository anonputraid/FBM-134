#!/usr/bin/python3
# -*- Author : Anonputraid -*-    
#
# This user interface provides users with a command console interface to the
# Framework.
#


class main:
    def initialize():
        from lib.core.api_common import banner
        banner()

    def CHANGELOG():
        from lib.core.api_common import version
        version()
        pass

    def HacktivityAction():
        from lib.core.api_options import console
        console()
        pass

    initialize()
    CHANGELOG() # Last Version
    HacktivityAction()
    pass

def main_control():
    pass

if __name__ == "__main__":
    main()


