import db as DB
import uuid
import modules.time as time
import data.settings as Settings


def CreateEvent(ID, Name, Type, A, B, Op, Data):
    cursor = DB.EventDB.cursor()
    cursor.execute(f"INSERT INTO events (ID, Name, Type, A, B, Op, Data) VALUES ('{ID}', '{Name}', '{Type}', '{A}', '{B}', '{Op}', '{Data}')")

    DB.EventDB.commit()

def FetchEvent(EID):
    cursor = DB.EventDB.cursor()
    cursor.execute(f"SELECT * FROM events WHERE ID = '{EID}'")
    event = cursor.fetchone()
    return event

def DeleteEvent(EID):
    cursor = DB.EventDB.cursor()
    cursor.execute(f"DELETE FROM events WHERE ID = '{EID}'")

    DB.EventDB.commit()

def ValidateTriggered(UID, EID):
    cursor = DB.EventDB.cursor()
    cursor.execute(f"SELECT * FROM users WHERE UID = '{UID}' AND EID = '{EID}'")
    event = cursor.fetchone()
    if event is None:
        return True
    else:
        cursor = DB.EventDB.cursor()
        cursor.execute(f"SELECT Type FROM events WHERE ID = '{EID}'")
        event = cursor.fetchone()
        
        if event == Settings.EVENT_TYPES["MultipleReddem"]:
            return False
        else:
            return True