#/usr/bin/python

# usage: test_arib_extra.py font-file 
# 2013-05-01/joshua zhan

from Tkinter import *
import tkFont

which = 0

texts = ['AaGg', 
	u'\ue0fe\ue2f4', 
	u'\u3402\u8a79']

fontfamilies = ('WadaLabMaruGo2004ARIB', 'Times New Roman')

def switchFontFamily():
	global which 
	which += 1
	which %= 2
	#print which, fontfamilies[which]
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
