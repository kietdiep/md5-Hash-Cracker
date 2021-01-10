import hashlib

wlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
hash2crack=input("hash: ")

#read file
wlistlines=open(wlist, "r").readlines()

#loop
for i in range(0, len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print("password found: "+wlistlines[i].replace("\n",""))
        exit()
print("password not found")