import Renamer as r

VideoDir = input('Whats the Video directory?\n')
VideoFileType = input('Whats the video file type?\n')
SubsFileType = input('Whats the substitles file type?\n')

VideoFile = r.SubRenamer(VideoDir,SubsFileType,VideoFileType)
VideoFile.RenameFile()