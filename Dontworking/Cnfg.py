global lol
lol = {}

def write(wh):
    with open('config.confg', 'a', encoding='utf-8') as c:
        c.write(f'{wh}\n')


def CONFG_PARSE():
    global lol
    with open('config.confg', 'r', encoding='utf-8') as c:
        data = c.readlines()
    j = 0
    for item in data:
        items = item.split()
        lol[j] = items[1]
        j = j + 1
        
