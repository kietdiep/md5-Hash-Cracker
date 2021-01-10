import hashlib

# open file and extract each line as attribute: username, hash function, salt, hash value of password
# create substrings of each to separate into dict() key and values(as lists)
# or possible create them as a class to indicate their different class objects ... not too sure on this one



# create a character list of all lower case letters,
# create all possible combinations of the characters and convert them to their hash forms 
# possibly store them into a list as a hash table for easy lookup
# check if the hash form matches the current hash we are looking at, if yes then output password to a list

# outer loop iterates n numbers of lines in file per acc
# inner loop will go through every iteration of the lower case combinations
# after variation, create the hash version of that, then check for match


# crypt = hashlib.md5()
# crypt.update(b"zhgnnd")              how to get basic hash but this is not what we are doing rn
# print(crypt.hexdigest())

hashfile = r"C:\Users\Kiet\Documents\md5\md5-Hash-Cracker\etc_shadow (sample)"

# Retrieve File will open the file and store everything into a dictionary, key = account name (team) , value = salt + hash password
def retrieveFile(hashfile):
    openfile = open(hashfile, 'r')
    hashDictTemp = dict()
    for account in openfile:
        accountList = account.split (':') 
        key = accountList[0]
        passwordHash = accountList[1]
        hashDictTemp[key] = passwordHash
    hashDictTemp.popitem() # this is here for now to delete the last 8 digit character that might take too long to do
    openfile.close()
    return(hashDictTemp)

def splitSaltnPass(hashDict):
    pass


hashDict = retrieveFile(hashfile)
print(len(hashDict))