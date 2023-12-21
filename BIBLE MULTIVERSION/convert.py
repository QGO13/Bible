from sqlite3 import *

chapitre = """

"""
chapitre=chapitre.replace("","chapiter__")
chapitre=chapitre.replace("chapiter__ ","¶")
chapitres = chapitre.split("¶")
connection = connect("BIBLE.db")
curseur = connection.cursor()
del chapitres[0]
for i in chapitres:
	print("\n\n")
	print(i)
	try:
		s1 = i[:3]
		s2 = i[3:]
		int(s1)
	except:
		s1 = i[:2]
		s2 = i[2:]
	finally:
		print(s1)
		print(len(s1))
	valeur = (s2, "", int(s1), "VERSION FRANCAISE LOUIS SECOND ")
	curseur.execute("""INSERT INTO "CHAPITER"("verse_content", "Book_name", "CHAPITER_Num", "nom_version") VALUES (?,?,?,?)""",valeur )
	connection.commit()
	print("ok")