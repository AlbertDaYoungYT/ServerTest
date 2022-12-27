import modules.BadgeEncryptionAlgo as BEA
import db as DB
import base64
import modules.time as time

def CreateBadge(Name, Description, Type, ImageID):
    cursor = DB.MainDB.cursor()

    (ID, cDate) = BEA.GenerateID()
    cursor.execute(f"INSERT INTO badges (BadgeID, UrlBadgeID, Name, Description, Type, ImageURL, CreationDate) VALUES ('{ID}', '{base64.urlsafe_b64encode(ID.encode()).decode()}', '{Name}', '{Description}', '{Type}', '/static/favicons/badges/{ImageID}', '{cDate}')")

    DB.MainDB.commit()
    return ID

def SetBadgeToUser(BID, UID):
    cursor = DB.MainDB.cursor()

    cursor.execute(f"INSERT INTO badgeowners (OwnerID, BadgeID, achievementDate) VALUES ('{UID}', '{BID}', '{time.utime()}')")

    DB.MainDB.commit()

def FetchUserBadges(UID):
    cursor = DB.MainDB.cursor()
    cursor.execute("SELECT * FROM badgeowners")
    results = cursor.fetchall()

    final = []
    for result in results:
        result = list(result)
        if result[0] == str(UID):
            final.append(result)
    
    return final

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

def CalculateRarity(Type, normal=True):
    if normal:
        cursor = DB.MainDB.cursor()
        cursor.execute("SELECT * FROM badges")
        results = cursor.fetchall()

        f_results = 0
        for result in results:
            result = list(result)
            if Type == result[4]:
                f_results += 1
        

        return (f_results / len(results)) * 100
    else:
        cursor = DB.MainDB.cursor()
        cursor.execute("SELECT * FROM badges")
        results = cursor.fetchall()

        f_results = 0
        f_amount = 0
        for result in results:
            result = list(result)
            if Type == result[4]:
                f_results += 1
            f_amount += 1
        
        if f_amount > 1000:
            suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion"]
            f_amount = "{:,}".format(f_amount)

            return f"{f_results} out of {' '.join(list((f_amount[:f_amount.find(',')], suffixes[f_amount.count(',')])))}"
        else:
            return f"{f_results} out of {f_amount}"