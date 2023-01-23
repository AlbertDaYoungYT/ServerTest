import os
import sqlite3
import modules.RealmMingle as RM



def PurgeDatabase():
    RM.UserDataDB.close()
    os.remove("./modules/RealmMingle/data.db")
    open("./modules/RealmMingle/data.db", "w")
    RM.UserDataDB = sqlite3.connect("modules/RealmMingle/data.db", check_same_thread=False)