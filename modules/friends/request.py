import modules.UserProfile as UP
import db as DB
import modules.time as time

def SendRequest(UID, FID):
    cursor = DB.NotificationDB.cursor()

    cursor.execute(f"INSERT INTO {UID} (ID, Notifier, Data, Type, Time) VALUES ('{FID}', '{UP.FetchUserdata(FID)[1]}', '0', 'FriendRQT', '{time.utime()}')")

    DB.NotificationDB.commit()

def CancelRequest(UID, FID):

def AcceptRequest(UID, FID):

def DenyRequest(UID, FID):