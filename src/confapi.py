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


class root:
	def cset(c):
         print(f"\033[38;5;{c}m")
	def bgset(c):
		print(f"\033[48;5;{c}m\033[2J\033[H", end="")


""" here we setting something """

class set:
	""" the blue one """
	def blue():
		root.cset(61)
		
	""" the green one """
	def green():
		root.cset(114)
		
	""" the red one """
	def red():
		root.cset(204)
