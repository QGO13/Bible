from customtkinter import *
from sqlite3 import *
import tkinter
from PIL import Image,ImageTk

def theme(apparance = "Dark", themes = "blue"):
	if switch_var.get() == "on" :
		apparance = "Dark"
		themes = "blue"
	else:
		apparance = "Light"
		themes = "green"
	set_appearance_mode(apparance)
	set_default_color_theme(themes)	

###########################################################################################################################
#fonction du menu principale

def menu_principale(background = "white"):
	def testaments(event):

		chapitre.configure(state = "disabled")
		messageBox.delete(1.0, END)
		if testament.get() != "Choisissez une option":
			livre.configure(state = "readonly")
			livre.set("Choisissez une option")
			curseur.execute("""SELECT * FROM LIVRE""")
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
		if livre.get() != "Choisissez une option":
			chapitre.configure(state = "readonly")
			chapitre.set("Choisissez une option")
			curseur.execute("""SELECT * FROM CHAPITRE""")
			CHap = curseur.fetchall()

			info__ = []
			for chap in CHap:
				if chap[2] == livre.get():
					info__.append(str(chap[3]))
			chapitre.configure(values = info__)

		else:
			chapitre.configure(state = "disabled")

	def chapitres(event):
		messageBox.delete(1.0, END)
		if chapitre.get() != "Choisissez une option":
			curseur.execute("""SELECT * FROM CHAPITRE""")
			CHap = curseur.fetchall()

			for chap in CHap:
				if chap[2] == livre.get() and chap[3] == int(chapitre.get()):
					messageBox.insert(1.0, chap[1])
					break

	



	curseur.execute("""SELECT * FROM TESTAMENT""")
	TESta = curseur.fetchall()

	info = []
	for testa in TESta:
		info.append(testa[0])
	# placer l'arriere plan 
	CTkLabel(app, text = "FRENCH BIBLE DARBI VERSION ", text_font = ("aharoni",20,'bold'), text_color = ("red", "green")).grid(row =0, column =0 , sticky="nw", columnspan = 5)
	CTkLabel(app, image = bg_image).grid(row=0, column = 5, sticky = "news")

	CTkLabel(app, text = "Testament", text_font = ("aharoni",16)).grid(row =0+1, column =0 , sticky="nw")
	CTkLabel(app, text = "Livre", text_font = ("aharoni",16)).grid(row =0+1, column = 2, sticky="nw")
	CTkLabel(app, text = "Chapitre", text_font = ("aharoni",16)).grid(row =0+1, column = 4, sticky="nw")



	message = tkinter.StringVar()
	messageBox = tkinter.Text(app, state = "normal", font = ("aharoni",16))
	messageBox.grid(row = 1+1, column = 0, columnspan = 32, rowspan = 20, sticky = "news")

	scrollbar = CTkScrollbar(app, command =messageBox.yview)
	scrollbar.grid(sticky = "ns", row = 2,column =33)
	messageBox.configure(yscrollcommand=scrollbar.set)
	livre = CTkComboBox(master=app,height = 35, state = "disabled", text_color =("green", "blue"), command = livres)
	chapitre = CTkComboBox(master=app,height = 35, state = "disabled", text_color =("green", "blue"), command = chapitres)
	chapitre.set("Choisissez une option")
	chapitre.grid(row=0+1, padx = 40, column=4+1, pady=10, sticky="swe")

	
	livre.set("Choisissez une option")
	livre.grid(row=0+1, padx = 40, column=2+1, pady=10, sticky="swe")

	testament = CTkComboBox(master=app,height = 35, values=info, state = "readonly", command =testaments,text_color =("green", "blue"))
	testament.set("Choisissez une option")
	testament.grid(row=0+1, padx = 40, column=0+1, pady=10, sticky="swe")


	
	
	switch_1 =CTkSwitch(master=app, 
							text="Theme", 
							command=theme,
					   variable=switch_var, 
					   onvalue="on", 
					   offvalue="off")
	switch_1.grid(row = 21+1, column = 0, sticky = "s", columnspan = 20)


PATH = os.path.dirname(os.path.realpath(__file__))
app = CTk()
app.title("""BIBLE FRENCH VERSION""")
app.geometry("1000x800")
app.minsize(700,700)
app.grid_rowconfigure((0,2), weight=10)
app.grid_columnconfigure((1,5,3), weight=1)
app.iconbitmap("L (1).ico")
switch_var =StringVar(value="on")
connection = connect("Bible_fr.db")
curseur = connection.cursor()
image = Image.open(PATH + "/L.png").resize((200,200))
bg_image = ImageTk.PhotoImage(image)
theme()
menu_principale()
#Application en boucle affichage de la fenetres 
app.mainloop()