import modules.blog.manager
global BlogDB
from __main__ import logger
logger.success("Blog module Initiated")

from datetime import date
import calendar
import sqlite3
import os

today = date.today()
Location = f"./data/blogs/{today.year}/{calendar.month_name[today.month]}/{today.day}/"
BlogDB = sqlite3.connect(Location + ".db", check_same_thread=False)

try:
    os.mkdir(f"./data/blogs/{today.year}/")
    os.mkdir(f"./data/blogs/{today.year}/{calendar.month_name[today.month]}/")
    os.mkdir(f"./data/blogs/{today.year}/{calendar.month_name[today.month]}/{today.day}/")

    cursor = BlogDB.cursor()
    for hour in range(1, 24+1):
        cursor.execute(f"CREATE TABLE '{str(hour)}' (`ID` TEXT NOT NULL,`Title` TEXT NOT NULL,`HTML` TEXT NOT NULL,`Genre` TEXT NOT NULL,`CreatorID` TEXT NOT NULL,`Date` INT NOT NULL)")

    BlogDB.commit()
except Exception as e:
    logger.error(f"Exception in creation './data/blogs/{today.year}/{calendar.month_name[today.month]}/{today.day}/': {e}")
