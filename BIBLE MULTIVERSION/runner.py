import PyInstaller.__main__


PyInstaller.__main__.run([
	'Bible multiversion.py',
	'--windowed',
    '--onefile',
    '--add-data=L1.png;img',
    '--add-data=L (1).ico;img',
    '--icon=L (1).ICO'
	])