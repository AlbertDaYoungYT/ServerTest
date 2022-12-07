import sqlite3

global db
db = sqlite3.connect("data/db.db", check_same_thread=False)