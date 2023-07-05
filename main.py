import Renamer as r
import options_chooser as oc
from tkinter import *

class RenamerUi:
    def __init__(self,window):
        FileTypes = ('.mp4')
        SubsTypes = ('.srt')
        LangTypes = ('English')    

        self.DirLbl = Label(window, text= "What's the Video directory?")
        self.SubLbl = Label(window, text= "What's the Subtitles file type?")
        self.VidLbl = Label(window, text= "What's the Video file type?")
        self.LanLbl = Label(window, text= "What's the subtitle language?")

        self.DirEnt = Entry()
        self.lbFiles = Listbox(window, height=1, selectmode='one')
        self.lbFiles.insert(1,FileTypes)
        self.lbSubs = Listbox(window, height=2, selectmode='multiple')
        self.lbSubs.insert(1,SubsTypes)
        self.lbLan = Listbox(window, height=2, selectmode='multiple')
        self.lbLan.insert(1,LangTypes)
        self.RenameSubs = Button(window, text='Rename Subtitles',command=self.Rename)

        self.DirLbl.place(x=20, y=50)
        self.SubLbl.place(x=20, y=100)
        self.VidLbl.place(x=20, y=150)
        self.LanLbl.place(x=20, y=200)
        self.DirEnt.place(x=200, y=50)
        self.lbFiles.place(x=200, y=100)
        self.lbSubs.place(x=200, y=150)
        self.lbLan.place(x=200, y=200)
        self.RenameSubs.place(x=20, y=250)
    def Rename(self):
        VideoDir = str(self.DirEnt.get())
        VideoFileType = str(self.lbFiles.get(1))
        SubsFileType = str(self.lbSubs.get(1))
        Language = str(self.lbLan.get(1))
        VideoFile = r.SubRenamer(VideoDir,SubsFileType,VideoFileType,Language)
        VideoFile.RenameFile()




#VideoInputDir = Entry(window, text='Whats the Video directory?',bd=5)
#VideoInputDir.place(x=80, y=150)
#VideoDir = lbl
#VideoDir = input('Whats the Video directory?\n')

# SubsFileType = oc.ChooseOption('Subtitle')
# VideoFileType = oc.ChooseOption('VideoFileType')
# Language = oc.ChooseOption('Language')

# VideoFile = r.SubRenamer(VideoDir,SubsFileType,VideoFileType,Language)
# VideoFile.RenameFile()
RenamerWin = Tk()
MyWin = RenamerUi(RenamerWin)
RenamerWin.title('Subtitle Renamer')
RenamerWin.geometry("500x300+10+10")
RenamerWin.mainloop()
