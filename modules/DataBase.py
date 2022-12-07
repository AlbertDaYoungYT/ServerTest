import db as DB
import time

def CreateUser(ID, Username, PwdHash):
    cursor = DB.db.cursor()
    cursor.execute(f"INSERT INTO users (ID, Username, PwdHash, CreationDate) VALUES ('{ID}', '{Username}', '{PwdHash}', '{time.time()}')")
    cursor.execute(f"INSERT INTO userdata (ID, DisplayName, ProfileIMG, isadmin) VALUES ('{ID}', '{Username}', 'default.png', 'False')")

    DB.db.commit()