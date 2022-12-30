import modules.UserProfile as UP
import db as DB
import modules.time as time

def CreateFriend(UID, FID):
    cursor = DB.FriendsDB.cursor()

    cursor.execute(f"INSERT INTO '{UID}' (ID, Username, FriendshipRank, DateMet) VALUES ('{FID}', '{UP.FetchUserdata(FID)[1]}', '0', '{time.utime()}')")
    cursor.execute(f"INSERT INTO '{FID}' (ID, Username, FriendshipRank, DateMet) VALUES ('{UID}', '{UP.FetchUserdata(UID)[1]}', '0', '{time.utime()}')")

    DB.FriendsDB.commit()

def DeleteFriend(UID, FID):
    cursor = DB.FriendsDB.cursor()

    cursor.execute(f"DELETE FROM '{UID}' WHERE ID = '{FID}'")
    cursor.execute(f"DELETE FROM '{FID}' WHERE ID = '{UID}'")

    DB.FriendsDB.commit()
