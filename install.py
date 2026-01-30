""" the file that just runs programm
    just use 
    python wallTUI.py <args>
"""
import os
"""maybe the code is unreadable """

f = os.path.expanduser("~/.bashrc")
n = "alias wall='python3 /usr/bin/sakura/src\n"

with open(full_path, 'a', encoding='utf-8') as f:
    f.write(f"\n{n}")