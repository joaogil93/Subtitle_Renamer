import os
import shutil

VideoDir = input('Whats the Video directory?\n')
VideoFileType = input('Whats the video file type?\n')
SubsFileType = input('Whats the substitles file type?\n')

os.chdir(VideoDir)
subsdir = GetSubfileDirectory(VideoDir)

filelist = os.listdir()
currdir = os.getcwd()
subsdir = currdir + '\\' + 'Subs'

for i in filelist:
    # print(i)
    if VideoFileType in i:
        FileName = i.replace(VideoFileType,'')
        # os.chdir(subsdir)
        os.chdir(subsdir +'\\'+ FileName)
        
        SubtitleFile = os.listdir()
        for k in SubtitleFile:
            print(k)
            if 'English.srt' in k:
                # print(k)
                SubsFileDir = subsdir +'\\'+ FileName + '\\' + k
                shutil.copyfile(SubsFileDir,currdir + '\\' + FileName + SubsFileType)

def GetSubfileDirectory(DirectoryToSearch):
    FolderList = os.listdir
    for j in DirectoryToSearch:
        if 'Subs' in j:
            return()