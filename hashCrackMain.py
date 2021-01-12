import binascii
import hashlib
import sys        # may not need


class ChadNKietOnCrack:
    b64="./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def string_tohex(insert params here):
        pass

    def get_intermediate(insert params here):
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

    def get_bytes(insert params here):
        pass

    def hash(genPass, salt):
        md5 = b"$1$"

        hashPass = self.get_intermediate(genPass, salt, md5)

        hashPass = self.get_bytes(genPass)

        hashPass = int(binascii.hexlify(hashPass), 16)

        encoded = ""
        for _ in range(22):
            encoded += self.b64[hashPass % 64]
            hashPass 
        
    
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