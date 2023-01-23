import sqlite3

global UserDataDB
UserDataDB = sqlite3.connect("modules/RealmMingle/data.db", check_same_thread=False)