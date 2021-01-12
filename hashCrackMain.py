import binascii
import hashlib
import sys        # may not need


class ChadNKietOnCrack:
    b64="./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def string_tohex(insert params here):
        pass

    def get_intermediate(self, password, salt, magic):
        inter = password + magic + salt
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

    def hash(insert params here):
        pass
    



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You forget to add the hash pass and salt")
        exit()

    inst = ChadNKietOnCrack()
    password, salt = sys.argv[1], sys.argv[2]

    ChadNKietMd5 = inst.hash(password, salt)            # subject to change

    print(ChadNKietMd5)






