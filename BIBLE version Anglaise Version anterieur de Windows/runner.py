import PyInstaller.__main__


PyInstaller.__main__.run([
	'Bible Anglaise By Goodness QUADRI.py',
	'--windowed',
    '--add-data=L.png;img',
    '--add-data=L (1).ico;img',
    '--add-data=BIBLE_En.db;db',
    '--icon=L (1).ICO'
	])

