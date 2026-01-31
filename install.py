""" the file that just runs programm
    just use 
    python wallTUI.py <args>
"""
import os
"""maybe the code is unreadable """
# we need to know where is bashrc
f = os.path.expanduser("~/.bashrc")
n = "alias wall='python3 /usr/bin/sakura/src\n"
# now writing alias
try:
    with open(full_path, 'a', encoding='utf-8') as f:
        f.write(f"\n{n}")
# if something wrong the except will appear
except:
    os.system('python src/scen/error.py')
