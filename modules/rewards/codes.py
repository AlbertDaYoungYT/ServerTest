import db as DB
import uuid
import modules.time as time
import modules.DataBase as Data
import modules.event as E

def RedeemCode(UID, code):
    cursor = DB.RewardsDB.cursor()
    cursor.execute(f"SELECT * FROM codes WHERE Code = '{code}'")
    code = cursor.fetchone()
    
    if Data.ValidateID(UID):
        if not E.manager.ValidateTriggered(UID, code[1]):
            E.trigger(code[1])
            return True
    else:
        return False

def CreateCode(A, B, Op, Reward, Type, Code, ExpireDate):
    ID = uuid.uuid4()
    E.manager.CreateEvent(ID, f"Event for {Code}", Type, A, B, Op, Reward)
    cursor = DB.RewardsDB.cursor()
    cursor.execute(f"INSERT INTO codes (Code, EID, DateInvalid) VALUES ('{Code}', '{ID}', '{ExpireDate}')")

    DB.EventDB.commit()

def DeleteCode(Code):
    cursor = DB.RewardsDB.cursor()
    cursor.execute(f"SELECT EID FROM codes WHERE Code = '{Code}'")
    EID = cursor.fetchone()
    
    E.manager.DeleteEvent(EID)
    cursor = DB.EventDB.cursor()
    cursor.execute(f"DELETE FROM codes WHERE Code = '{Code}'")

    DB.EventDB.commit()