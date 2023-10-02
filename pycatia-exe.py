# !/usr/bin/python3.10

"""
This script is strictly for the use of generating the pycatia.exe executable.
"""

import argparse
import sys
import textwrap
from pathlib import Path
from pycatia.version import version

if __name__ == "__main__":

    prog = "pycatia"

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        =====================================================================
                                 pycatia
        =====================================================================
           This executable is currently provided for testing purposes only.
        Documentation: https://pycatia.readthedocs.io/en/latest/
        =====================================================================
        '''),
        prog=prog,
        usage="pycatia.exe file_name.py")

    parser.add_argument("filename",
                        type=str,
                        help="The full path filename of the python script file.")
    parser.add_argument('--version', action='version', version=f'{prog} {version}')

    filename = Path(parser.parse_args().filename)

    if filename.exists():

        import pycatia

        exec(open(filename).read())
    else:
        raise FileNotFoundError(f'Could not find file "{filename}". Try using the full path name.')
