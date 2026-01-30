# =============
#   argparse  
# =============

""" 
   here we can do one argument (not one)
   if one of the args is 
        - --blue
        - --red
        - --green
   it will change colors
   also you can call
        - --help
   
   the confapi is just
   a colors set
   scen folder is a folder
   for scenarios
   like --help 
"""

import sys
import confapi

import platform

""" checks sys.args """
if platform.system() == "Windows":
    import os
    os.system('')
for item in sys.argv:
	if item == "--blue":
		confapi.set.blue()
	if item == "--red":
		confapi.set.red()
	if item == "--green":
		confapi.set.green()
	if item == "--help":
		import scen.help
	
