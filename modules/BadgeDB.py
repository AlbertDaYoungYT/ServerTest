import db as DB
import hashlib
import time

def CreateBadge(Name, Description, ImageID):
    cursor = DB.MainDB.cursor()

    ID = hashlib.sha3_256(str(time.time()).encode()).hexdigest()
    cursor.execute(f"INSERT INTO badges (BadgeID, Name, Description, ImageURL, CreationDate) VALUES ('{ID}', '{Name}', '{Description}', '/static/favicons/badges/{ImageID}', '{time.time()}')")

    DB.MainDB.commit()

def SetBadgeToUser(BID, UID):
    cursor = DB.MainDB.cursor()

    cursor.execute(f"INSERT INTO badgeowners (OwnerID, BadgeID, achievementDate) VALUES ('{UID}', '{BID}', '{time.time()}')")

    DB.MainDB.commit()

def FetchUserBadges(UID):
    cursor = DB.MainDB.cursor()
    cursor.execute("SELECT * FROM badgeowners")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[0] == UID:
            return result
    
    return "NOTFOUND"

def FetchAllBadges():
    cursor = DB.MainDB.cursor()
    cursor.execute("SELECT * FROM badges")
    results = cursor.fetchall()

    f_results = []
    for result in results:
        result = list(result)
        f_results.append(result)
    
    return f_results

def FetchBadge(BID):
    cursor = DB.MainDB.cursor()
    cursor.execute("SELECT * FROM badges")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[0] == BID:
            return result
    
    return "NOTFOUND"
