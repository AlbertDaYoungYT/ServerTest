from Cryptodome.Util.Padding import pad
from Cryptodome.Cipher import AES
from requests import get
from base64 import *
import platform
import hashlib
import time


def GenerateID():
    time_of_creation = time.time()
    ip = get('https://api.ipify.org').content.decode('utf8')
    data_for_encrypt = [platform.machine(),
                        platform.uname().node,
                        platform.system(),
                        ip,
                        "pepepopo"
                    ]

    final = []
    for item in data_for_encrypt:
        for char in item:
            final.append(ord(char))
        final.append(1)

    nfinal = []
    sm = set(final)
    for x in final:
        if x != 1:
            nfinal.append(x-sorted(sm)[1] + 2)
        else:
            nfinal.append(x)
    final = nfinal
    
    merged = ""
    for integer in final:
        merged += "{0:0=2d}".format(integer)

    key = hashlib.md5(str(time_of_creation).encode('utf-8')).hexdigest()

    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv=b"0123456789abcdef")
    padded_data = pad(b64encode(merged.encode()) + b"\x00", cipher.block_size)
    return b85encode(cipher.encrypt(padded_data)).decode(), time_of_creation


def DecodeID(ID, time_of_creation):
    key = hashlib.md5(str(time_of_creation).encode('utf-8')).hexdigest()

    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv=b"0123456789abcdef")
    ID = b64decode(cipher.decrypt(b85decode(ID.encode())).split(b"=")[0] + b"=").decode()
    ID = [ID[i:i+2] for i in range(0, len(ID), 2)]
    one_locs = [i for i, x in enumerate(ID) if x == "01"]
    ID = [i for i in ID if i != "01"]
    ID1 = []
    for itera in range(100):
        ID1 = [ chr(int(x) + itera) for x in ID]
        try:
            if ''.join(ID1[0:5]) == "AMD64" or ''.join(ID1[0:3]) == "x86":
                ID = ID1
                break
            else:
                pass
        except Exception:
            pass

    [ ID.insert(loc, " ") for loc in one_locs]
    ID = ''.join(ID).split()

    return ID