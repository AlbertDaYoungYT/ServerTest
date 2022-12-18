import modules.UserProfile as UP
import db as DB
import time

def CreateFriend(UID, FID):
    cursor = DB.FriendsDB.cursor()

    cursor.execute(f"INSERT INTO {UID} (ID, Username, FriendshipRank, DateMet) VALUES ('{FID}', '{UP.FetchUserdata(FID)[1]}', '0', '{time.time()}')")

    DB.FriendsDB.commit()

def DeleteFriend(UID, FID):
    cursor = DB.FriendsDB.cursor()

    cursor.execute(f"INSERT INTO {UID} (ID, Username, FriendshipRank, DateMet) VALUES ('{FID}', '{UP.FetchUserdata(FID)[1]}', '0', '{time.time()}')")

    DB.FriendsDB.commit()
