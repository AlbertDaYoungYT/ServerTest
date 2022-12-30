import modules.UserProfile as UP
import db as DB
import hashlib
import uuid
import modules.time as time


def FetchNotifiers(UID):
    cursor = DB.NotificationDB.cursor()
    cursor.execute(f"SELECT * FROM '{UID}'")
    results = cursor.fetchall()

    f_results = []
    for result in results:
        result = list(result)
        f_results.append(result)
    
    return f_results



def SendRequest(UID, FID):
    cursor = DB.NotificationDB.cursor()

    ID = hashlib.md5((uuid.uuid1().hex).encode()).hexdigest()

    cursor.execute(f"INSERT INTO '{FID}' (ID, Notifier, Data, Res, Type, Time) VALUES ('{ID}', '<b title=\"{UID}\" style=\"cursor: pointer;\">{UP.FetchUserdata(UID)[1]}</b> sent You a Friend Request', '{UID}', 'None', 'FriendRQT', '{time.time()}')")

    DB.NotificationDB.commit()

def CancelRequest(UID, FID):
    cursor = DB.NotificationDB.cursor()

    cursor.execute(f"DELETE FROM '{FID}' WHERE Data = '{UID}'")

    DB.NotificationDB.commit()

def VerifyRequest(UID, FID):
    cursor = DB.NotificationDB.cursor()
    cursor.execute(f"SELECT * FROM '{FID}'")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if str(result[2]) == UID:
            return True
    
    return False