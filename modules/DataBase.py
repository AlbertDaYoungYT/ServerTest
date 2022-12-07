import db as DB
import time

def CreateUser(ID, Username, PwdHash):
    cursor = DB.db.cursor()
    cursor.execute(f"INSERT INTO users (ID, Username, PwdHash, CreationDate) VALUES ('{ID}', '{Username}', '{PwdHash}', '{time.time()}')", val)

    DB.db.commit()