from tkinter import *
from tkinter import filedialog
from pygame import mixer
mixer.init()
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

#Global var
totalsonglength=0

def musicUrl():
	try:
		dd=filedialog.askopenfilename(initialdir='C:/Users/Mausam/Music/Songs',
			title='select audio file',
			filetype=(('MP3','*mp3'),('WAV','*wav')))
		#print(dd)
	except:
		dd=filedialog.askopenfilename(filetype=(('MP3','*mp3'),('WAV','*wav')))
	audiotrack.set(dd)
def playMusic():
	ad=audiotrack.get()
	mixer.music.load(ad)
	mixer.music.play()
	audioStatusLabel.configure(text='Playing')
	ProgressbarLabel.grid()
	root.muteButton.grid()
	mixer.music.set_volume(0.4)
	ProgressbarVolume['value']=40
	ProgressbarVolumeLabel['text']='40%'
	ProgressbarMusicLabel.grid()

	Song=MP3(ad)
	totalsonglength=int(Song.info.length)
	ProgressbarMusic['maximum']=totalsonglength
	ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
	def Progressbarmusictick():
		CurrentSongLength=mixer.music.get_pos()//1000
		ProgressbarMusic['value']=CurrentSongLength
		ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
		ProgressbarMusic.after(2,Progressbarmusictick)
	Progressbarmusictick()
def pauseMusic():
	mixer.music.pause()
	root.PauseButton.grid_remove()
	root.ResumeButton.grid()
	audioStatusLabel.configure(text='Resuming')
def resumeMusic():
	mixer.music.unpause()
	root.ResumeButton.grid_remove()
	root.PauseButton.grid()
	audioStatusLabel.configure(text='Playing')
def volumeUp():
	vol=mixer.music.get_volume()
	if(vol>=vol*100):
		mixer.music.set_volume(vol+0.1)
	else:
		mixer.music.set_volume(vol+0.05)
	ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
	ProgressbarVolume['value']=mixer.music.get_volume()*100
def volumeDown():
	vol=mixer.music.get_volume()
	if(vol<=vol*100):
		mixer.music.set_volume(vol-0.1)
	else:
		mixer.music.set_volume(vol-0.05)
	ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
	ProgressbarVolume['value']=mixer.music.get_volume()*100
def unmuteMusic():
	global currentvol
	root.unmuteButton.grid_remove()
	root.muteButton.grid()
	mixer.music.set_volume(currentvol)
def muteMusic():
	global currentvol
	root.muteButton.grid_remove()
	root.unmuteButton.grid()
	currentvol=mixer.music.get_volume()
	mixer.music.set_volume(0)

def stopMusic():
	mixer.music.stop()
	audioStatusLabel.configure(text='Stopping')
#creating this function to add buttons and other important modules
def createwidthes():
	#Global variable 
	global audiotrack
	audiotrack=StringVar()
	global currentvol
	currentvol=0
	global playIcon,pauseIcon,browseIcon,volumeUpIcon,volumeDownIcon,muteIcon,unmuteIcon,stopIcon,resumeIcon
	global audioStatusLabel,ProgressbarLabel,ProgressbarVolume,ProgressbarVolumeLabel,ProgressbarMusicLabel,ProgressbarMusicStartTimeLabel,ProgressbarMusicEndTimeLabel,ProgressbarMusic
	#Image Icon Addition in Button and Label
	playIcon=PhotoImage(file='play-button.png')
	pauseIcon=PhotoImage(file='pause.png')
	browseIcon=PhotoImage(file='search-engine.png')
	volumeUpIcon=PhotoImage(file='volume-up.png')
	volumeDownIcon=PhotoImage(file='volume-down.png')
	muteIcon=PhotoImage(file='mute.png')
	unmuteIcon=PhotoImage(file='unmute.png')
	stopIcon=PhotoImage(file='stop.png')
	resumeIcon=PhotoImage(file='resume.png')
	#Changing image size of icons
	playIcon=playIcon.subsample(12,12)
	pauseIcon=playIcon.subsample(12,12)
	browseIcon=browseIcon.subsample(12,12)
	volumeUpIcon=volumeUpIcon.subsample(12,12)
	volumeDownIcon=volumeDownIcon.subsample(12,12)
	muteIcon=muteIcon.subsample(12,12)
	unmuteIcon=unmuteIcon.subsample(12,12)
	stopIcon=stopIcon.subsample(12,12)
	resumeIcon=resumeIcon.subsample(12,12)

	TrackLabel=Label(root,text='Audio Track Menu',background='lightskyblue',font=('arial',15,'italic bold'),width=20) 
	TrackLabel.grid(row=0,column=0,padx=20,pady=20)

	TrackLabelEntry=Entry(root,background='lightskyblue',font=('arial',15,'italic bold'),width=30,textvariable=audiotrack) 
	TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

	BrowseButton=Button(root,text='Search Music',background='yellow',bd=5,activebackground='purple',font=('arial',15,'italic bold'),width=200,image=browseIcon,compound=RIGHT,command=musicUrl)      #command is used here to make clickable button 
	BrowseButton.grid(row=0,column=2,padx=20,pady=20)

	PlayButton=Button(root,text='Play',background='orange',bd=5,activebackground='purple4',font=('arial',15,'italic bold'),width=200,image=playIcon,compound=RIGHT,command=playMusic)
	PlayButton.grid(row=1,column=0,padx=20,pady=20)

	StopButton=Button(root,text='Stop',background='red',bd=5,activebackground='purple4',font=('arial',15,'italic bold'),width=200,image=stopIcon,compound=RIGHT,command=stopMusic)
	StopButton.grid(row=2,column=0,padx=20,pady=20)

	root.PauseButton=Button(root,text='Pause',background='lightgreen',bd=5,activebackground='purple4',font=('arial',15,'italic bold'),width=200,image=pauseIcon,compound=RIGHT,command=pauseMusic)
	root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

	root.ResumeButton=Button(root,text='resume',background='red',bd=5,activebackground='purple',font=('arial',15,'italic bold'),width=200,image=resumeIcon,compound=RIGHT,command=resumeMusic)
	root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
	root.ResumeButton.grid_remove()

	VolumeUpButton=Button(root,text='Volume Up',background='orange',bd=5,activebackground='purple4',font=('arial',15,'italic bold'),width=200,image=volumeUpIcon,compound=RIGHT,command=volumeUp)
	VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

	VolumeDownButton=Button(root,text='Volume Down',background='red',bd=5,activebackground='purple4',font=('arial',15,'italic bold'),width=200,image=volumeDownIcon,compound=RIGHT,command=volumeDown)
	VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

	root.muteButton=Button(root,text='Mute',width=100,bg='yellow',activebackground='purple4',bd=5,image=muteIcon,compound=RIGHT,command=muteMusic)
	root.muteButton.grid(row=3,column=3)
	root.muteButton.grid_remove()

	root.unmuteButton=Button(root,text='UnMute',width=100,bg='yellow',activebackground='purple4',bd=5,image=unmuteIcon,compound=RIGHT,command=unmuteMusic)
	root.unmuteButton.grid(row=3,column=3)
	root.unmuteButton.grid_remove()

	audioStatusLabel=Label(root,text='',background='lightskyblue',font=("arial",15,"italic bold"),width=20)
	audioStatusLabel.grid(row=2,column=1)

	#Progress-bar
	ProgressbarLabel=Label(root,text='',bg='red')
	ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
	ProgressbarLabel.grid_remove()

	ProgressbarVolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=190)
	ProgressbarVolume.grid(row=0,column=0,ipadx=5)

	ProgressbarVolumeLabel=Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
	ProgressbarVolumeLabel.grid(row=0,column=0)

	ProgressbarMusicLabel=Label(root,text='',bg='red')
	ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)

	ProgressbarMusicStartTimeLabel=Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=8)
	ProgressbarMusicStartTimeLabel.grid(row=0,column=0)

	ProgressbarMusicEndTimeLabel=Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=8)
	ProgressbarMusicEndTimeLabel.grid(row=0,column=2)

	ProgressbarMusic=Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
	ProgressbarMusic.grid(row=0,column=1,ipadx=300,ipady=3)
	ProgressbarMusicLabel.grid_remove()
#Global variable declaration

#Container for app 
root=Tk()
root.geometry('1050x500+100+100')
root.title('Corona Music App Player')
root.iconbitmap('kingbondl.ico')
root.resizable(False,False) 
root.configure(bg='lightskyblue')
createwidthes()
StringText='App Developer - KingbondL / MS'
count=0
text=''
SliderLabel=Label(root,text=StringText,bg='lightskyblue',font=('arial',15,'italic bold'))
SliderLabel.grid(row=4,padx=20,pady=20,columnspan=3)
def StringTextSliderShow():
	global count,text
	if(count>=len(StringText)):
		count=-1
		text=''
		SliderLabel.configure(text=text)
	else:
		text=text+StringText[count]
		SliderLabel.configure(text=text)
	count+=1
	SliderLabel.after(200,StringTextSliderShow)
StringTextSliderShow()
root.mainloop() 
