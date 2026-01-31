""" here we storing colors and configuration
    you can use the own one
    just set the color by calling
    cset(color)
    there is 256 colors
    different terminals = different colors
"""

# ===========
# !   root  !
# ===≈=======

""" root is a commands to set something """
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "conf", "data.json")

with open(file_path, "r") as f:
    pamparam = json.load(f)

class root:
	def cset(c):
         print(f"\033[38;5;{c}m")
	def bgset(c):
		print(f"\033[48;5;{c}m\033[2J\033[H", end="")


""" here we setting something """

class set:
	""" the blue one """
	def blue():
		try:
		    root.cset(pamparam['blue'])
		except:
		    root.cset(61)
		
	""" the green one """
	def green():
		try:
		    root.cset(pamparam['green'])
		except:
		    root.cset(114)
		
	""" the red one """
	def red():
		try:
		    root.cset(pamparam['red'])
		except:
		    root.cset(204)
