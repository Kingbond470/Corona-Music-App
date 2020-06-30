from cx_Freeze import *
includefiles=['kingbondl.ico','end.png','microphone.png','mute.png','pause.png','play-button.png','resume.png','search-engine.png','stop.png','unmute.png','volume-up.png','volume-down.png','music_app.py']
excludes=[]
packages=[]
base=None
if sys.platform=='win32':
	base='Win32GUI'
shortcut_table=[(
	'DesktopShortcut', #Shortcut
	'DesktopFolder', #Directory_
	'Corona Music App', #Name
	'TARGETDIR', #Component_
	'[TARGETDIR]\music_app.exe', #Target
	None, #Arguments
	None, #Description
	None, #Hottkey
	None, #Icon
	None, #IconIndex
	None, #ShowCmd
	'TARGETDIR', #WkDir
	)
]
msi_data={'Shortcut':shortcut_table}
bdist_msi_options={'data':msi_data}
setup(
	version='0.1',
	Description='It is a beta version of Corona Music Player and It is developed for educational purpose.If you have any other project ideas or some modification required in this application then you can contact me on my social account social account: insta-kingbondl,github-kingbond470,twitter-@mausamsingh470',
	author='Mausam Singh',
	name='KingbondL Music Player',
	options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
	executables=[
	Executable(
		script='music_app.py',
		base=base,
		icon='kingbondl.ico',
		)
	]
)