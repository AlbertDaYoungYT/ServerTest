import modules.UserProfile as UP
import db as DB


def Delete(UID, NID):
    cursor = DB.NotificationDB.cursor()

    cursor.execute(f"DELETE FROM '{UID}' WHERE ID = '{NID}'")

    DB.NotificationDB.commit()

def VerifyNotification(UID, NID):
    cursor = DB.NotificationDB.cursor()
    cursor.execute(f"SELECT * FROM '{UID}'")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if str(result[0]) == NID:
            return True
    
    return False