import db as DB
import modules.time as time

def Add(ID, Email):
    cursor = DB.MainDB.cursor()
    cursor.execute(f"INSERT INTO subscribtions (ID, Email, Data, DateAdded) VALUES ('{ID}', '{Email}', '', '{time.utime()}')")

    DB.MainDB.commit()

def Remove(ID):
    cursor = DB.MainDB.cursor()
    cursor.execute(f"DELETE FROM subscribtions WHERE ID = '{ID}'")

    DB.MainDB.commit()