import hashlib

# create a character list of all lower case letters,
# create all possible combinations of the characters and convert them to their hash forms 
# possibly store them into a list as a hash table for easy lookup
# check if the hash form matches the current hash we are looking at, if yes then output password to a list

def initialize(createdPass,md5,salt):
    res = createdPass + md5 + salt
    cryptVal = hashlib.md5()
    cryptVal.update(bytes(res, 'ascii'))            #problem will most likely be in here due to the difference in md5 * ask questions later and maybe chabo will find the way
    length = len(createdPass)
    while length > 0 :
        res = res + cryptVal[0:min(16,length)]
        length = length - 16
    i = len(createdPass)
    while i != 0:
        if i and 1:
            res += '\x00'
        else:
            res += password[0]
                                       

def passGenerator():
    pass

def ifValid(createdPass, givenPass):
    pass
# crypt = hashlib.md5()
# crypt.update(b"zhgnnd")             * how to get basic hash but this is not what we are doing rn
# print(crypt.hexdigest())



md5 = hashDict["team0"][0:3] # this stores $1$
salt = hashDict["team0"][3:11] #  stores hfT7jp2q$

# will use hashDict later for comparisons

createdPass = "zhgnnd"
#print(initialize(createdPass,md5,salt))













# hashfile = r"C:\Users\Kiet\Documents\md5\md5-Hash-Cracker\etc_shadow (sample)"

# # Retrieve File will open the file and store everything into a dictionary, key = account name (team) , value = salt + hash password
# def retrieveFile(hashfile):
#     openfile = open(hashfile, 'r')
#     hashDictTemp = dict()
#     for account in openfile:
#         accountList = account.split (':') 
#         key = accountList[0]
#         passwordHash = accountList[1]
#         hashDictTemp[key] = passwordHash
#     hashDictTemp.popitem() # this is here for now to delete the last 8 digit character that might take too long to do
#     openfile.close()
#     return(hashDictTemp)

# # take in inputs of hashDict and split md5 salt and hash password
# # in this case we know that the md5 will be the first 3 characters of the hashDict value so we can just create a substring of everything after
# # Additionally we can create a substring of everything after the first 12 because we will know the salt after just extracting one of the strings

# # team0:$1$hfT7jp2q$wPwz7GC6xLt9eQZ9eJkaq.:16653:0:99999:7:::

# def splitSaltnPass(hashDict):
#     tempHashDict = dict()
#     for key in hashDict:
#         hashPass = hashDict[key][12:]
#         tempHashDict[key] = hashPass
#     return tempHashDict

# hashDict = retrieveFile(hashfile)
# hashDict = splitSaltnPass(hashDict)   #hashDict contains key = team , value = hash password