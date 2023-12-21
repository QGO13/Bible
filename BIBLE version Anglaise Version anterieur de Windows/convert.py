from sqlite3 import *

chapitre ="""

"""
chapitre=chapitre.replace("Chapter ","¶")
chapitres = chapitre.split("¶")
print(chapitres)
connection = connect("BIBLE_En_.db")
curseur = connection.cursor()
del chapitres[0]
for i in chapitres:
	print("\n\n")
	print(i)
	s1 = i[:2]
	s1 = s1[-2:]
	print(s1)
	s2 = i[4:]
	print(len(s1))
	valeur = (s2, "", int(s1))
	curseur.execute("""INSERT INTO "CHAPITER"("verse_content", "Book_name", "CHAPITER_Num") VALUES (?,?,?)""",valeur )
	connection.commit()
	print("ok")