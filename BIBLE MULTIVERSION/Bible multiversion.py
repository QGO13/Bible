from sqlite3 import *
from tkinter import *
from tkinter import ttk

import os

###########################################################################################################################
#fonction du menu principale

def menu_principale(background = "white"):
	def versions(event):
		testament.configure(state = "readonly")
		if testa_com.get() == "":
			testament.set("Choisissez une option")
		chapitres(event)
	def testaments(event):

		chapitre.configure(state = "disabled")
		messageBox.delete(1.0, END)
		if testament.get() != "Choisissez une option":
			livre.configure(state = "readonly")
			livre.set("Choisissez une option")
			curseur.execute("""SELECT * FROM BOOK""")
			LIVres = curseur.fetchall()

			info_ = []
			for Livres in LIVres:
				if Livres[1] == testament.get():
					info_.append(Livres[0])
			livre.configure(values = info_)

		else:
			livre.configure(state = "disabled")
						
					


	def livres(event):
		messageBox.delete(1.0, END)
		if livre.get() != "Choisissez une option" :
			chapitre.configure(state = "readonly")
			chapitre.set("Choisissez une option")
			curseur.execute("""SELECT * FROM CHAPITER""")
			CHap = curseur.fetchall()

			info__ = []
			for chap in CHap:
				if chap[2] == livre.get() and chap[-1] == version_com.get():
					info__.append(str(chap[3]))
			chapitre.configure(values = info__)

		else:
			chapitre.configure(state = "disabled")

	def chapitres(event):
		messageBox.delete(1.0, END)
		if chapitre.get() != "Choisissez une option":
			curseur.execute("""SELECT * FROM CHAPITER""")
			CHap = curseur.fetchall()

			for chap in CHap:
				if chap[2] == livre.get() and chap[3] == int(chapitre.get()) and chap[-1] == version_com.get():
					messageBox.insert(1.0, chap[1])
					break

	def Button_fonction():
		messageBox.delete(1.0, END)
		if chapitre.get() != "Choisissez une option":
			curseur.execute("""SELECT * FROM CHAPITER""")
			CHap = curseur.fetchall()

			for chap in CHap:
				if chap[2] == livre.get() and chap[3] == int(chapitre.get()) and chap[-1] == version_com.get():
					messageBox.insert(1.0, chap[1])
					break
	



	curseur.execute("""SELECT * FROM TESTAMENT""")
	TESta = curseur.fetchall()

	info = []
	for testa in TESta:
		info.append(testa[0])
	curseur.execute("""SELECT * FROM VERSION""")
	Vers = curseur.fetchall()
	Version = []
	for Ver in Vers:
		Version.append(Ver[0])

	# placer l'arriere plan 
	Label(app, text = "BIBLE MULTIVERSION ", font = ("aharoni",20,'bold')).grid(row =0, column =0 , sticky="nw", columnspan = 5)
	Label(app, image = bg_image).grid(row=0, column = 5, sticky = "news")

	Label(app, text = "Testament", font = ("aharoni",16)).grid(row =20+1, column =0 , sticky="nw")
	Label(app, text = "Book", font = ("aharoni",16)).grid(row =20+1, column = 2, sticky="nw")
	Label(app, text = "Chapiter", font = ("aharoni",16)).grid(row =20+1, column = 4, sticky="nw")



	message = StringVar()
	messageBox = Text(app, state = "normal", font = ("aharoni",16))
	messageBox.grid(row = 1, column = 0, columnspan = 32, rowspan = 20, sticky = "news")

	scrollbar = Scrollbar(app, command =messageBox.yview)
	scrollbar.grid(sticky = "ns", row = 1,column =33, rowspan = 20)
	messageBox.configure(yscrollcommand=scrollbar.set)
	livre_com = StringVar()
	livre = ttk.Combobox(master=app,height = 35, textvariable = livre_com, state = "disabled")
	livre.bind('<<ComboboxSelected>>', livres)

	chapitre_com = StringVar()
	chapitre = ttk.Combobox(master=app,height = 35, textvariable = chapitre_com,state = "disabled")
	chapitre.bind('<<ComboboxSelected>>', chapitres)
	chapitre.set("Choisissez une option")
	chapitre.grid(row=20+1, padx = 40, column=4+1, pady=10, sticky="swe")

	
	livre.set("Choisissez une option")
	livre.grid(row=20+1, padx = 40, column=2+1, pady=10, sticky="swe")
	testa_com = StringVar()
	testament = ttk.Combobox(master=app,height = 35, values=info, state = "disabled", textvariable = testa_com)
	testament.bind('<<ComboboxSelected>>', testaments)
	testament.set("Choisissez une option")
	testament.grid(row=20+1, padx = 40, column=0+1, pady=10, sticky="swe")

	Label(app, text = "VERSION ", font = ("aharoni",16)).grid(row =0, column =0 , sticky="ew", columnspan = 2)
	version_com = StringVar()
	version = ttk.Combobox(app, height = 75, values = Version, state = "readonly", textvariable = version_com)
	version.bind('<<ComboboxSelected>>', versions)
	version.set("Choisissez une option")
	version.grid(row = 0, column = 2, columnspan = 3, sticky ="ew")
	Button(app, text = "RAFFRAICHIR LE CONTENUE", command = Button_fonction).grid(row = 0, column = 1, columnspan = 3, sticky = "ws")
	




PATH = os.path.dirname(os.path.realpath(__file__))
app = Tk()
app.title("""BIBLE ENGLISH VERSION""")
app.geometry("1000x800")
app.minsize(700,700)
app.grid_rowconfigure((0,2), weight=10)
app.grid_columnconfigure((1,5,3), weight=1)
app.iconbitmap("L (1).ico")
switch_var =StringVar(value="on")
connection = connect("BIBLE.db")
curseur = connection.cursor()

bg_image =PhotoImage(file = "L1.png")
menu_principale()
#Application en boucle affichage de la fenetres 
app.mainloop()