import modules.BagdeEncryptionAlgo as BEA
import db as DB
import json


def AddDev(ID, oauth):
    cursor = DB.DeveloperDB.cursor()
    cursor.execute(f"INSERT INTO devs (ID, OAuth, CreationDate) VALUES ('{ID}', '{oauth}', '{time.utime()}')")
    cursor.execute(f"CREATE TABLE `{oauth}` (`LogType` TEXT NOT NULL,`Log` TEXT NOT NULL,`Time` INT NOT NULL)")

    DB.DeveloperDB.commit()

def RemoveDev(ID):
    cursor = DB.DeveloperDB.cursor()
    cursor.execute(f"DELETE FROM devs WHERE ID = '{ID}'")
    cursor.execute(f"DROP TABLE IF EXISTS '{ID}'")

    DB.DeveloperDB.commit()

def ValidateDev(ID, oauth):
    cursor = DB.DelevoperDB.cursor()
    cursor.execute(f"SELECT OAuth FROM devs WHERE ID = '{ID}' AND OAuth = '{oauth}'")
    event = cursor.fetchone()
    
    if event is not None:
        cursor = DB.DelevoperDB.cursor()
        cursor.execute(f"INSERT INTO '{oauth}' (LogType, Log, Time) VALUES ('VALIDATIONINFO', 'Validation Success', '{time.utime()}')")
        DB.DelevoperDB.commit()

        return True
    else:
        cursor = DB.DelevoperDB.cursor()
        cursor.execute(f"INSERT INTO '{oauth}' (LogType, Log, Time) VALUES ('VALIDATIONINFO', 'Validation Failed', '{time.utime()}')")
        DB.DelevoperDB.commit()

        return False

def GenerateOAuthToken(Client, Signer, *args):
    return BEA.GenrateCustom(Signer, Client, CustomMessage="OAUTHTOKEN", *args)


def ConstructJson(function, data):
    return _json


def HandleRequest(_json):
    if _json["METHOD"] == "POST":
        return POST(_json)
    elif _json["METHOD"] == "GET":
        return GET(_json)


def GET(_json):
    if ValidateDev(_json["ID"], _json["OAuth"]):
        func = _json["Function"]
        var = eval(_json["Variables"])
        return json.dumps(exec(eval(func + f"(*eval({var}))")))
    else:
        return json.dumps({"error": 403})


def POST(json):
    if ValidateDev(json["ID"], json["OAuth"]):
        func = json["Function"]
        var = eval(json["Variables"])
        return json.dumps(exec(eval(func + f"(*eval({var}))")))
    else:
        return json.dumps({"error": 403})