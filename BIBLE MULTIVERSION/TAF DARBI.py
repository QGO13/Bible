from sqlite3 import *


connection_rec = connect("BIBLE.db")
curseur_rec = connection_rec.cursor()

connection_send = connect("Bible_fr.db")
curseur_send = connection_send.cursor()

curseur_send.execute("""SELECT * FROM CHAPITRE""")

chapitre_send = curseur_send.fetchall()
chapitre_send_list = []
for i in chapitre_send:
	i_list = list(i)
	chapitre_send_list.append(i_list)

for i in chapitre_send_list:
	i.append("VERSION FRANCAISE DARBI")
	if i[2] == "Genèse":
		i[2] = "Genesis"
	elif i[2] == "Exode":
		i[2] = "Exodus"
	elif i[2] == "Lévitique":
		i[2] = "Leviticus"
	elif i[2] == "Nombres":
		i[2] = "Numbers"
	elif i[2] == "Deutéronome":
		i[2] = "Deuteronomy"
	elif i[2] == "Josué":
		i[2] = "Joshua"
	elif i[2] == "Juges":
		i[2] = "Judges"
	elif i[2] == "Ruth":
		i[2] = "Ruth"
	elif i[2] == "1 Samuel":
		i[2] = "1 Samuel"
	elif i[2] == "2 Samuel":
		i[2] = "2 Samuel"
	elif i[2] == "1 Rois":
		i[2] = "1 Kings"
	elif i[2] == "2 Rois":
		i[2] = "2 Kings"
	elif i[2] == "1 Chroniques":
		i[2] = "1 Chronicles"
	elif i[2] == "2 Chroniques":
		i[2] = "2 Chronicles"
	elif i[2] == "Esdras":
		i[2] = "Ezra"
	elif i[2] == "Néhémie":
		i[2] = "Nehemiah"
	elif i[2] == "Esther":
		i[2] = "Esther"
	elif i[2] == "Job":
		i[2] = "Job"
	elif i[2] == "Psaumes":
		i[2] = "Psalms"
	elif i[2] == "Proverbes":
		i[2] = "Proverbs"
	elif i[2] == "Ecclésiaste ":
		i[2] = "Ecclesiastes "
	elif i[2] == "Cantique ":
		i[2] = "Song of Songs "
	elif i[2] == "Esaïe":
		i[2] = "Isaiah"
	elif i[2] == "Jérémie":
		i[2] = "Jeremiah"
	elif i[2] == "Lamentations":
		i[2] = "Lamentations"
	elif i[2] == "Ezéchiel":
		i[2] = "Ezekiel"
	elif i[2] == "Daniel":
		i[2] = "Daniel"
	elif i[2] == "Osée":
		i[2] = "Hosea"
	elif i[2] == "Joël":
		i[2] = "Joel"
	elif i[2] == "Amos":
		i[2] = "Amos"
	elif i[2] == "Abdias":
		i[2] = "Obadiah"
	elif i[2] == "Jonas":
		i[2] = "Jonah"
	elif i[2] == "Michée ":
		i[2] = "Micah "
	elif i[2] == "Nahum":
		i[2] = "Nahum"
	elif i[2] == "Habacuc":
		i[2] = "Habakkuk"
	elif i[2] == "Sophonie":
		i[2] = "Zephaniah"
	elif i[2] == "Aggée":
		i[2] = "Haggai"
	elif i[2] == "Zacharie":
		i[2] = "Zechariah"
	elif i[2] == "Malachie":
		i[2] = "Malachi"
	elif i[2] == "Matthieu":
		i[2] = "Matthew"
	elif i[2] == "Marc":
		i[2] = "Mark"
	elif i[2] == "Luc":
		i[2] = "Luke"
	elif i[2] == "Jean":
		i[2] = "John"
	elif i[2] == "Actes":
		i[2] = "Acts"
	elif i[2] == "Romains":
		i[2] = "Romans"
	elif i[2] == "1 Corinthiens":
		i[2] = "1 Corinthians"
	elif i[2] == "2 Corinthiens":
		i[2] = "2 Corinthians"
	elif i[2] == "Galates":
		i[2] = "Galatians"
	elif i[2] == "Ephésiens":
		i[2] = "Ephesians"
	elif i[2] == "Philippiens":
		i[2] = "Philippians"
	elif i[2] == "Colossiens":
		i[2] = "Colossians"
	elif i[2] == "1 Thessaloniciens":
		i[2] = "1 Thessalonians"
	elif i[2] == "2 Thessaloniciens":
		i[2] = "2 Thessalonians"
	elif i[2] == "1 Timothée":
		i[2] = "1 Timothy"
	elif i[2] == "2 Timothée":
		i[2] = "2 Timothy"
	elif i[2] == "Tite":
		i[2] = "Titus"
	elif i[2] == "Philémon":
		i[2] = "Philemon"
	elif i[2] == "Hébreux":
		i[2] = "Hebrews"
	elif i[2] == "Jacques":
		i[2] = "James"
	elif i[2] == "1 Pierre":
		i[2] = "1 Peter"
	elif i[2] == "2 Pierre":
		i[2] = "2 Peter"
	elif i[2] == "1 Jean":
		i[2] = "1 John"
	elif i[2] == "2 Jean":
		i[2] = "2 John"
	elif i[2] == "3 Jean":
		i[2] = "3 John"
	elif i[2] == "Jude":
		i[2] = "Jude"
	elif i[2] == "Apocalypse":
		i[2] = "Revelation"
	del i[0]
chapitre_send_tuple = []
for x in chapitre_send_list:
	x_tuple = tuple(x)
	chapitre_send_tuple.append(x_tuple)

curseur_rec.executemany("""INSERT INTO "CHAPITER"("verse_content", "Book_name", "CHAPITER_Num", "nom_version") VALUES (?,?,?,?)""",chapitre_send_tuple)
print("ok")
connection_rec.commit()
print("ok")
	
