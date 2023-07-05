import os
import shutil



class SubRenamer():

    def __init__(self,VideoDir,SubsFileType,VideoFileType,SubLanguage):
        
        self.VideoDirectory = VideoDir
        self.SubsType = SubsFileType
        self.VideoType = VideoFileType
        self.Language = SubLanguage
        

    def RenameFile(self):
        
        try:
            os.chdir(self.VideoDirectory)
        except:
            print('The directory was not found.')
            exit
        
        filelist = os.listdir()
        currdir = os.getcwd()
        subsdir = currdir + '\\' + 'Subs'
        
        for i in filelist:
            
            if self.VideoType in i:
                FileName = i.replace(self.VideoType,'')
                
                try:
                    os.chdir(subsdir +'\\'+ FileName)
                except:
                    print('The directory was not found.')
                    exit

                SubtitleFile = os.listdir()
                for k in SubtitleFile:
                    SubLanguage = self.Language + self.SubsType
                    if SubLanguage in k:
                        
                        SubsFileDir = subsdir +'\\'+ FileName + '\\' + k
                        shutil.copyfile(SubsFileDir,currdir + '\\' + FileName + self.SubsType)