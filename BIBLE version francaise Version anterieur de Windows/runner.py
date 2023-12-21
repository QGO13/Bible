import PyInstaller.__main__


PyInstaller.__main__.run([
	'Bible Francaise By Goodness QUADRI.py',
	'--windowed',
    '--add-data=L.png;img',
    '--add-data=L (1).ico;img',
    '--add-data=Bible_Fr.db;db',
    '--icon=L (1).ICO'
	])

