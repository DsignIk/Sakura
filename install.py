""" the file that just runs programm
    just use 
    python wallTUI.py <args>
"""
import os
import platform

dir = os.getcwd()
os.system(f'mv "{dir}" /usr/bin/sakura')

"""maybe the code is unreadable """
# if os is the Linux using bashrc
if platform.system() == 'Linux':
    f = os.path.expanduser("~/.bashrc")
    
    n = "alias sakura='python3 /usr/bin/sakura/src'" 
    try:
        with open(f, 'a', encoding='utf-8') as l:
            l.write(f"\n{n}\n")
    except:
        os.system('python3 /usr/bin/sakura/src/scen/error.py')

# if os is the FreeBSD using cshrc
if platform.system() == 'FreeBSD':
    f = os.path.expanduser("~/.cshrc")
    
    n = "alias sakura 'python3 /usr/bin/sakura/src/main.py'"
    
    try:
        with open(f, 'a', encoding='utf-8') as bsd:
            bsd.write(f"\n{n}\n")
    except:
        os.system('python3 /usr/bin/sakura/src/scen/error.py')
