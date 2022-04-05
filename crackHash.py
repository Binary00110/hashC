import hashlib
import os
from colorama import Fore,init
init()

def clear():
    if os.name == 'nt':
        os.system("cls")
        print(Fore.CYAN+"| Binary00110 | Github : https://github.com/Binary00110/ \n")
    elif os.name == 'posix':
        os.system("clear")
        print(Fore.CYAN+"| Binary00110 | Github : https://github.com/Binary00110/ \n")

clear()
print(f"""{Fore.YELLOW}Select the desired option: 
   1. MD5
   2. SHA-1
   3. SHA256 
   4. SHA224
   5. SHA512
   6. SHA384
    """)

choice = input(Fore.CYAN+">>> "+Fore.GREEN)

clear()
hash_file_list = input(Fore.YELLOW+"Hash File : "+Fore.CYAN)
pass_file_list = input(Fore.YELLOW+"Password File : "+Fore.CYAN)
clear()

try:
    hash_file = open(hash_file_list).read().splitlines()
    pass_file = open(pass_file_list).read().splitlines()
except:
    pass
def crackHash(hashFile , passwdFile , method):
    inde = 0
    for ha in hashFile:
        for passwd in passwdFile:
            Become_hash = method(passwd.encode()).hexdigest()
            if(Become_hash == ha):
                print(Fore.YELLOW+f"{ha} : {Fore.GREEN}{passwd}")
            else:
                inde +=1
                print("{} password tested .".format(inde),end="\r")
                
if choice == '1':
    crackHash(hashFile=hash_file , passwdFile=pass_file , method=hashlib.md5)
elif choice == '2':
    crackHash(hashFile=hash_file , passwdFile=pass_file , method=hashlib.sha1)
elif choice == '3':
    crackHash(hashFile=hash_file , passwdFile=pass_file , method=hashlib.sha256)
elif choice == '4':
    crackHash(hashFile=hash_file , passwdFile=pass_file , method=hashlib.sha224)
elif choice == '5':
    crackHash(hashFile=hash_file , passwdFile=pass_file , method=hashlib.sha512)
elif choice == '5':
    crackHash(hashFile=hash_file , passwdFile=pass_file , method=hashlib.sha512)
elif choice == '6':
    crackHash(hashFile=hash_file , passwdFile=pass_file , method=hashlib.sha384)
else:
    print(Fore.RED+"Error ....")