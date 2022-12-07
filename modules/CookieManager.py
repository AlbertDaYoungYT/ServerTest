import db as DB
import _thread as thread
import random
import string
import time

def randstr(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))



def CreateCookieID():
    cursor = DB.db.cursor()
    ID = randstr(64)

    cursor.execute(f"INSERT INTO cookies (cookieid, expires) VALUES ('{ID}', '{time.time() + (10)}')")
    DB.db.commit()

    return ID


def CheckCookie(ID):
    CookieDelete()
    cursor = DB.db.cursor()

    cursor.execute("SELECT * FROM cookies")

    results = cursor.fetchall()
    for result in results:
        if ID in result:
            return "VALID"
    
    return "INVALID"


def CookieDelete():
    cursor = DB.db.cursor()

    cursor.execute("SELECT * FROM cookies")

    results = cursor.fetchall()
    for result in results:
        result = list(result)
        if result[-1] < time.time():
            cursor = DB.db.cursor()
            cursor.execute(f"DELETE FROM cookies WHERE cookieid = '{result[0]}'")
            DB.db.commit()