import binascii
import hashlib
import sys       

class ChadNKietOnCrack:
    b64="./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def get_alternate(self, password, salt):
        return hashlib.md5(password + salt + password).hexdigest()

    def get_hashPass(self, password, salt, md5):
        hashPass = password + md5 + salt
        alternate = self.get_alternate(password, salt)
        pass_len = len(password)

        xalternate = binascii.unhexlify(alternate)
        for i in range(pass_len, 0, -16):
            hashPass += xalternate[0:16 if i > 16 else i]

        while pass_len:
            if pass_len & 1:
                hashPass += chr(0).encode()
            else:
                hashPass += password[0:1]
            
            pass_len >>= 1

        return hashlib.md5(hashPass).hexdigest()

    def loop(self, hashPass, password, salt):
        for i in range(1000):
            alternate = b""
            if i % 2: alternate += password
            else: alternate += hashPass

            if (i % 3) != 0: alternate += salt

            if (i % 7) != 0: alternate += password

            if i % 2: alternate += hashPass
            else: alternate += password

            hashPass = hashlib.md5(alternate).digest()

        return hashPass

    def get_bytes(self, hashPass):
        response = b""
        idx = [11, 4, 10, 5, 3, 9, 15, 2, 8, 14, 1, 7, 13, 0, 6, 12]
        for x in idx:
            response += hashPass[x:x + 1]
        
        return response


    def hash(self, password, salt):
        md5 = b"$1$"

        # compute the initial hashPass value
        hashPass = self.get_hashPass(password, salt, md5)

        # loop 
        hashPass = self.loop(binascii.unhexlify(hashPass), password, salt)

        # swap bytes according to the given idx list
        hashPass = self.get_bytes(hashPass)

        # hex to int
        hashPass = int(binascii.hexlify(hashPass), 16)

        # int to base64
        encoded = ""
        for _ in range(22):
            encoded += self.b64[hashPass % 64]
            hashPass //= 64

        return encoded
        
    
    def generateCombo(self, password, salt):
        lowalph = "abcdefghijklmnopqrstuvwxyz"
        for i in lowalph:
            for j in lowalph:
                for k in lowalph:   
                    for l in lowalph:
                        for m in lowalph:
                            for n in lowalph:
                                tempStr = i+j+k+l+m+n
                                print(tempStr)
                                etempStr = tempStr.encode()
                                if self.hash(etempStr, salt) == password:
                                    return tempStr

                                
                            

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You forget to add the hash pass and salt")
        exit()

    inst = ChadNKietOnCrack()
    #password, salt = sys.argv[1].encode(), sys.argv[2].encode()
    #ChadNKietMd5 = inst.hash(password, salt)
    password, salt = sys.argv[1], sys.argv[2].encode()
    ChadNKietMd5 = inst.generateCombo(password, salt)            # subject to change hash -> generate combo

    print(ChadNKietMd5)