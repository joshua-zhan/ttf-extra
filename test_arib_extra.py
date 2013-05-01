#/usr/bin/python

# usage: just run it
#
# tested on Ubuntu 13.04
# python2.7 with python-tk module
#
# 2013-05-01/joshua zhan

from Tkinter import *
import tkFont

texts = ['AaGg', 
	u'\ue0fe\ue2f4', 
	u'\u3402\u8a79']

which = 0

fontfamilies = ('WadaLabMaruGo2004ARIB', 
		'Times New Roman',
		'Ubuntu')

def switchFontFamily():
	global which 
	which += 1
	which %= len(fontfamilies) 
	print which, fontfamilies[which]
	labelfont = (fontfamilies[which], 32, 'normal')
	children = tk.winfo_children()
	for w in children:
		if isinstance(w, Label):
			w.config(font = labelfont)

tk = Tk()
tk.title('ARIB EXTRA CHARS')

Button(tk, text = 'Switch Font Family', command = switchFontFamily).pack()

labelfont = (fontfamilies[which], 32, 'normal')
for tt in texts:
	widget = Label(tk, text = tt)
	widget.config(font = labelfont)
	widget.config(height = 2, width = 20)
	widget.pack()

tk.mainloop()
