import sqlite3

global MainDB
global ChallengesDB
MainDB = sqlite3.connect("data/main.db", check_same_thread=False)
ChallengesDB = sqlite3.connect("data/challenges.db", check_same_thread=False)