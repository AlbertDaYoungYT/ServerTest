import db as DB
import time

def FetchUserdata(ID):
    cursor = DB.db.cursor()
    cursor.execute("SELECT * FROM userdata")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[0] == str(ID):
            return result
    
    return "NOTFOUND"