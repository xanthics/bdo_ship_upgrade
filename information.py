from browser.html import *


def gen_info():
	ret = H2("Upgrade Paths") + BR() + CANVAS(id='shipchart', width=820, height=400) + BR()
	ret += "This" + BR() + "is a " + STRONG("Placeholder")
	return ret