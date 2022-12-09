import db as DB
import time

def FetchTheme(ID):
    cursor = DB.MainDB.cursor()
    cursor.execute("SELECT * FROM themes")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[0] == str(ID):
            return result
    
    return "NOTFOUND"

def FetchDefaultTheme():
    ID = "default"
    cursor = DB.MainDB.cursor()
    cursor.execute("SELECT * FROM themes")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[0] == str(ID):
            return result
    
    return "NOTFOUND"