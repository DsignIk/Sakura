import os
import sys



SHELL_NAME = os.getenv('SHELL')
OS_TERM = os.getenv('TERM')
OS_TERM_PROG = os.getenv('TERM_PROGRAM')
TTY_OS_NAME = os.ttyname(sys.stdout.fileno())
