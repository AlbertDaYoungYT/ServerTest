import db as DB
import uuid
import modules.time as time


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