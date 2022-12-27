import db as DB
import modules.time as time

def FetchUserdata(ID):
    cursor = DB.MainDB.cursor()
    cursor.execute("SELECT * FROM userdata")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[0] == str(ID):
            return result
    
    return "NOTFOUND"

def FetchEUserdata(ID):
    cursor = DB.MainDB.cursor()
    cursor.execute("SELECT * FROM euserdata")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[0] == str(ID):
            return result
    
    return "NOTFOUND"


def UpdateUserdata(Uid, Address, Email, Phone, Fullname, DisplayName, Description):
    cursor = DB.MainDB.cursor()
    cursor.execute(f"UPDATE euserdata SET Address = '{Address}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE euserdata SET Email = '{Email}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE euserdata SET Phone = '{Phone}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE euserdata SET Fullname = '{Fullname}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE userdata SET DisplayName = '{DisplayName}' WHERE ID = '{Uid}'")
    cursor.execute(f"UPDATE userdata SET Description = '{Description}' WHERE ID = '{Uid}'")
    DB.MainDB.commit()