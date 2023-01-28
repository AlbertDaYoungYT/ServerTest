import sqlite3
from __main__ import logger

global UserDataDB
UserDataDB = sqlite3.connect("modules/RealmMingle/data.db", check_same_thread=False)
logger.success("RealmMingle module Initiated")