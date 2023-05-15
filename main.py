import Renamer as r
import options_chooser as oc

VideoDir = input('Whats the Video directory?\n')

SubsFileType = oc.ChooseOption('Subtitle')
VideoFileType = oc.ChooseOption('VideoFileType')
Language = oc.ChooseOption('Language')

VideoFile = r.SubRenamer(VideoDir,SubsFileType,VideoFileType,Language)
VideoFile.RenameFile()