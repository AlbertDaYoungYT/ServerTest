import sqlite3

global MainDB
global SitesDB
global ChallengesDB
global NotificationDB
global FriendsDB
MainDB = sqlite3.connect("data/main.db", check_same_thread=False)
SitesDB = sqlite3.connect("data/sites.db", check_same_thread=False)
ChallengesDB = sqlite3.connect("data/challenges.db", check_same_thread=False)
NotificationDB = sqlite3.connect("data/notifications.db", check_same_thread=False)
FriendsDB = sqlite3.connect("data/friends.db", check_same_thread=False)