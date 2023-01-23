import db as DB
import modules.time as time

def CreateUser(ID, DisplayName, Username, PwdHash, bday):
    cursor = DB.MainDB.cursor()
    cursor.execute(f"INSERT INTO users (ID, Email, MigleName, Bio, Gender, SexualPreference, Birthday, Links, Places) VALUES ('{ID}', '{Username}', '{PwdHash}', '{time.utime()}')")
    cursor.execute(f"CREATE TABLE '{ID}' (`Type` TEXT NOT NULL,`DataA` TEXT NOT NULL,`Op` TEXT NOT NULL,`DataB` TEXT NOT NULL,`Date` INT NOT NULL)")

    DB.MainDB.commit()

def FetchUser(ID):
    cursor = DB.MainDB.cursor()
    cursor.execute(f"SELECT * FROM users WHERE ID = '{ID}'")
    results = cursor.fetchone()

    return results

def FetchData(ID):
    cursor = DB.MainDB.cursor()
    cursor.execute(f"SELECT * FROM {ID}")
    results = cursor.fetchone()

    return results

def UpdateUser(Uid, Address, Email, Phone, Fullname, DisplayName, Description):
    cursor = DB.MainDB.cursor()
    cursor.execute(f"UPDATE users SET Address = '{Address}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE users SET Email = '{Email}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE users SET Phone = '{Phone}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE users SET Fullname = '{Fullname}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE users SET DisplayName = '{DisplayName}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE users SET Description = '{Description}' WHERE ID = '{Uid}'")
    DB.MainDB.commit()

def DeleteUser(ID):
    cursor = DB.EventDB.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS '{ID}'")
    cursor.execute(f"DELETE * FROM users WHERE ID = '{ID}'")

    DB.EventDB.commit()