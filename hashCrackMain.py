import binascii
import hashlib
import sys        # may not need


class ChadNKietOnCrack:
    b64="./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def string_tohex(insert params here):
        pass

    def get_intermediate(insert params here):
        pass

    def loop(insert params here):
        pass

    def get_bytes(insert params here):
        pass

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






