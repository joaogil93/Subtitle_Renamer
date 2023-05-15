import os
import shutil



class SubRenamer():

    def __init__(self,VideoDir,SubsFileType,VideoFileType):
        
        self.VideoDirectory = VideoDir
        self.SubsType = SubsFileType
        self.VideoType = VideoFileType

        

    def RenameFile(self):
        
        os.chdir(self.VideoDirectory)
        
        filelist = os.listdir()
        currdir = os.getcwd()
        subsdir = currdir + '\\' + 'Subs'
        
        for i in filelist:
            
            if self.VideoType in i:
                FileName = i.replace(self.VideoType,'')
                
                os.chdir(subsdir +'\\'+ FileName)
                
                SubtitleFile = os.listdir()
                for k in SubtitleFile:
                    
                    if 'English.srt' in k:
                        
                        SubsFileDir = subsdir +'\\'+ FileName + '\\' + k
                        shutil.copyfile(SubsFileDir,currdir + '\\' + FileName + self.SubsType)