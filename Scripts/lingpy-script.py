#!c:\users\user\palaung\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'lingpy==2.6.6','console_scripts','lingpy'
__requires__ = 'lingpy==2.6.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('lingpy==2.6.6', 'console_scripts', 'lingpy')()
    )
