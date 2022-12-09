import db as DB
import time

def CreateUser(ID, DisplayName, Username, PwdHash):
    cursor = DB.db.cursor()
    cursor.execute(f"INSERT INTO users (ID, Username, PwdHash, CreationDate) VALUES ('{ID}', '{Username}', '{PwdHash}', '{time.time()}')")
    cursor.execute(f"INSERT INTO userdata (ID, DisplayName, ProfileIMG, Description, Coins, isadmin) VALUES ('{ID}', '{DisplayName}', 'default.png', '', 0, 'False')")

    DB.db.commit()

def ValidateUser(Username, PwdHash):
    cursor = DB.db.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[1] == Username and result[2] == PwdHash:
            return True
    
    return False

def ValidateID(ID):
    cursor = DB.db.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[0] == ID:
            return True
    
    return False

def FetchUID(Username, PwdHash):
    cursor = DB.db.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[1] == Username and result[2] == PwdHash:
            return result[0]
    
    return False
