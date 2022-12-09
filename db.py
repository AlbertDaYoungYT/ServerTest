import sqlite3

global MainDB
MainDB = sqlite3.connect("data/main.db", check_same_thread=False)