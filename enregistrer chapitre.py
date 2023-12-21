from customtkinter import *
from sqlite3 import *




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

def enregistre(entry1, entry2, combobox_1):
	if entry1.get().replace(" ","") != "" and entry2.get().replace(" ","") != "" and combobox_1.get() != "Choisissez une option":
		valeur = (entry2.get(), combobox_1.get(), int(entry1.get()))
		curseur.execute("""INSERT INTO CHAPITRE ("Verset_du_chapitre", "Nom_livre", "numero_chapitre") VALUES (?,?,?)""",valeur )
		connection.commit()
		entry1.delete(0,"end")
		entry2.delete(0,"end")
		

def menu_principale(background = "white"):

	# placer le bouton de connection 
	curseur.execute("""SELECT * FROM LIVRE""")
	livres = curseur.fetchall()
	print(livres)
	info = []
	for livre in livres:
		info.append(livre[0])

	combobox_1 = CTkComboBox(master=app,height = 35, values=info, state = "readonly", text_color =("green", "blue"))
	combobox_1.set("Choisissez une option")
	combobox_1.grid(row=0, padx = 40, column=0, pady=10, sticky="we", columnspan = 15)

	entry1 = CTkEntry(master=app,
					   placeholder_text="Numero",
					   width=200,
					   height=30,
					   border_width=2,
					   corner_radius=10)
	entry1.grid(row = 1, column = 0,sticky = "nesw")
	entry2 = CTkEntry(master=app,
					   placeholder_text="Chapitre",
					   width=200,
					   height=30,
					   border_width=2,
					   corner_radius=10)
	entry2.grid(row = 1, column = 1,sticky = "nesw", columnspan = 5)
	button = CTkButton(master=app, 
							text="ENREGISTER LE CHAPITRE", 
							command=lambda : enregistre(entry1,entry2,combobox_1), 
							padx = 3, 
							pady = 2,  
							fg_color = "green", 
							text_color = "white")
	button.grid(row = 2, column = 5, columnspan = 2)
	switch_1 =CTkSwitch(master=app, 
							text="Theme", 
							command=theme,
					   variable=switch_var, 
					   onvalue="on", 
					   offvalue="off")
	switch_1.grid(row = 3, column = 0, sticky = "s", columnspan = 20)










app = CTk()
app.title("""BIBLE FRENCH VERSION""")
app.geometry("1000x800")
app.minsize(700,700)
app.grid_rowconfigure((0,1,2), weight=1)
app.grid_columnconfigure((1,2,3), weight=1)
switch_var =StringVar(value="on")
connection = connect("Bible_fr.db")
curseur = connection.cursor()
theme()
menu_principale()
#Application en boucle affichage de la fenetres 
app.mainloop()