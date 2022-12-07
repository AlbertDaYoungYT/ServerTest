import db as DB
import random
import string
import time

def randstr(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

def CreateCookieID():
    cursor = DB.db.cursor()
    ID = randstr(64)

    cursor.execute("INSERT INTO cookies (cookieid, expires) VALUES (%s, %s)", (ID, time.time() + (60 * 60 * 12)))

    return ID


def CheckCookie(ID):
    

