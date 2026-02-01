""" 
    this is the Logger
    its make the log.txt
    in your current directory
    so don't recommend to
    use install because
    install is bad
"""


import sys
import os


def down():
    with open('log.txt', 'a', encoding='utf-8') as idk:
        idk.write('[-] something was wrong with your download\n')

def load(pack):
    with open('log.txt', 'a', encoding='utf-8') as idk:
        idk.write(f'[+] loading {pack}\n')
        
def succes():
    with open('log.txt', 'a', encoding='utf-8') as idk:
        idk.write("[+] success in downloading file\n")
        
