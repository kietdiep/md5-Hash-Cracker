import binascii
import hashlib
import sys        # may not need


class ChadNKietOnCrack:
    b64="./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def string_tohex(insert params here):
        pass

    def get_intermediate(self, password, salt, magic):
        inter = password + magic + salt
        alternate = hashlib.md5(password + salt + password).hexdigest()
        pass_len = len(password)

        xalt = binascii.unhexlify(alternate)
        for i in range (pass_len, 0, -16):
            inter +=  xalt[0:16 if i > 16 else i]

        while pass_len:
            if pass_len & 1:
                inter += chr(0).encode()
            else:
                inter += password[0:1]
            
            pass_len >>= 1
        
        return hashlib.md5(inter).hexdigest()
        
        pass

    def loop(password, salt, h):
        for i in range (1000):
            tmp =""
            if i % 2:
                tmp += password
            else:
                tmp += h

            if (i % 3)==0:
                tmp += salt

            if (i % 7)==0:
                tmp += password

            if i % 2:
                tmp += h
            else:
                tmp += password

            fin = hashlib.md5(h).digest()

        return fin


    def get_bytes(self, bytes):
        temp = b""
        idx = [11, 4, 10, 5, 3, 9, 15, 2, 8, 14, 1, 7, 13, 0, 6, 12]
        for i in idx:
            temp += bytes[x:x+1]

        return bytes

    def hash(genPass, salt):
        md5 = b"$1$"

        hashPass = self.get_intermediate(genPass, salt, md5)

        hashPass = self.get_bytes(genPass)

        hashPass = int(binascii.hexlify(hashPass), 16)

        encoded = ""
        for _ in range(22):
            encoded += self.b64[hashPass % 64]
            hashPass //= 64
        
        return md5.decode() + salt.decode() + '$' + encoded
        
    
    def generateCombo(self, password, salt):
        LowAlpha = "abcdefghijklmnopqrsuvwxyz"
        tempStr = ""
        for char1 in LowAlpha:
            tempStr.append(char1)
            for char2 in LowAlpha:
                tempStr.append(char2)
                for char3 in LowAlpha:
                    tempStr.append(char3)
                    for char4 in LowAlpha:
                        tempStr.append(char4)
                        for char5 in LowAlpha:
                            tempStr.append(char5)
                            for char6 in LowAlpha:
                                tempStr.append(char6)
                                etempStr = tempStr.encode()
                                if hash(etempStr, salt) == password:
                                    return tempStr 
                                




if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You forget to add the hash pass and salt")
        exit()

    inst = ChadNKietOnCrack()
    password, salt = sys.argv[1], sys.argv[2].encode()

    ChadNKietMd5 = inst.generateCombo(password, salt)            # subject to change hash -> generate combo

    print(ChadNKietMd5)