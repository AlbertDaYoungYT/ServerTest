import db as DB
import uuid
import modules.time as time

def RedeemCode(UID, code):
    cursor = DB.RewardsDB.cursor()
    cursor.execute(f"SELECT * FROM codes WHERE Code = '{code}'")
    code = cursor.fetchone()
    return event