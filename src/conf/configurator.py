""" 
    this installer
    is not ready to use
    when new function will added
    this configuration will be ready
"""


""" 
    in this configurator
    you can chose
    y or n
    if you chose y to
    function it will
    write True in json
"""



import json
import sys
import os

data = {
    "browser": False,
    "blue": 61,
    "red": 204,
    "green": 114
}

bo = []
print ("               configuration")
print ("[*] emulate browser?")

# ye this works bad but its works
# so okay

a = input ('[Y/N] ')

# starting if else slop

if a == "Y":
    bo.append("browser")
    print ("[+] custom user agent = user-agent-installer")
if a == "y":
    bo.append("browser")
    print ("[+] custom user agent = user-agent-installer")
if a == "n":
    bo.append("nobrowser")
if a == "N":
    bo.append("nobrowser")

""" settings """
print ("[*] you need to set colors?")

# ========
#  colors 
# ========

a = input('[y/n] ')

if a == "y":
    print ("[!] YOU NEED ANSI 256 COLORS")
    red = input("[red] ")
    green = input("[green] ")
    blue = input("[blue] ")
    data["blue"] = blue
    data["green"] = green
    data["red"] = red
    
print ("[+] Color set end")

for item in bo:
    match item:
        case "browser":
            print ("[+] setting browser emulate")
            data["browser"] = True
        case "nobrowser":
            print ("[+] setting browser to no")
            data['browser'] = False


# writing json data to data.json
# the most unreadable thing I wrote
# this is about json writing

a = input('[!] this programm is only for downloading! press Y to continue ')
if a == "Y":
    pass
else:
    print ("[!] THIS IS ONLY FOR DOWNLOADING!")
    sys.exit(0)
    
with open("data.json", "w", encoding="utf-8") as file:
    print ("writing json")
    json.dump(data, file, indent=4, ensure_ascii=False)
    
