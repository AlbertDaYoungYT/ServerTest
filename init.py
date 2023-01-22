import os

os.remove("./data/friends.db")
os.remove("./data/notifications.db")
open("./data/friends.db", "w")
open("./data/notifications.db", "w")


import db as DB

mycursor = DB.MainDB.cursor()

mycursor.execute("DROP TABLE IF EXISTS users")
mycursor.execute("DROP TABLE IF EXISTS themes")
mycursor.execute("DROP TABLE IF EXISTS badges")
mycursor.execute("DROP TABLE IF EXISTS userdata")
mycursor.execute("DROP TABLE IF EXISTS euserdata")
mycursor.execute("DROP TABLE IF EXISTS badgeowners")
mycursor.execute("DROP TABLE IF EXISTS subscribtions")
mycursor.execute("CREATE TABLE `users` (`ID` TEXT NOT NULL,`Username` TEXT NOT NULL,`PwdHash` TEXT NOT NULL,`CreationDate` INT NOT NULL)")
mycursor.execute("CREATE TABLE `themes` (`Name` TEXT NOT NULL,`color1` TEXT NOT NULL,`color2` TEXT NOT NULL,`color3` TEXT NOT NULL,`color4` TEXT NOT NULL,`color5` TEXT NOT NULL,`color6` TEXT NOT NULL,`color7` TEXT NOT NULL)")
mycursor.execute("CREATE TABLE `userdata` (`ID` TEXT NOT NULL,`DisplayName` TEXT NOT NULL,`ProfileIMG` TEXT NOT NULL,`Description` TEXT NOT NULL,`Birthday` INT NOT NULL,`GCoins` INT NOT NULL,`Credits` INT NOT NULL,`isadmin` TEXT NOT NULL)")
mycursor.execute("CREATE TABLE `euserdata` (`ID` TEXT NOT NULL,`Address` TEXT NOT NULL,`Phone` TEXT NOT NULL,`Email` TEXT NOT NULL,`Fullname` TEXT NOT NULL)")

mycursor.execute("CREATE TABLE `badges` (`BadgeID` TEXT NOT NULL,`UrlBadgeID` TEXT NOT NULL,`Name` TEXT NOT NULL,`Description` TEXT NOT NULL,`Type` TEXT NOT NULL,`ImageURL` TEXT NOT NULL,`CreationDate` INT NOT NULL)")
mycursor.execute("CREATE TABLE `badgeowners` (`OwnerID` TEXT NOT NULL,`BadgeID` TEXT NOT NULL,`achievementDate` INT NOT NULL)")

mycursor.execute("CREATE TABLE `subscribtions` (`OwnerID` TEXT NOT NULL,`Email` TEXT NOT NULL,`Data` TEXT NOT NULL,`DateAdded` INT NOT NULL)")


mycursor.execute("INSERT INTO themes (Name, color1, color2, color3, color4, color5, color6, color7) VALUES ('default', '#212836', '#C9C8C8', '#086080', '#141820', '#2596BE', '#1C212E', '#77819A')")

DB.MainDB.commit()


mycursor = DB.ChallengesDB.cursor()

mycursor.execute("DROP TABLE IF EXISTS allc")
mycursor.execute("DROP TABLE IF EXISTS users")

mycursor.execute("CREATE TABLE `allc` (`CID` TEXT NOT NULL,`Name` TEXT NOT NULL,`Trigger` TEXT NOT NULL,`Image` TEXT NOT NULL,`Reward` INT NOT NULL,`CreationDate` INT NOT NULL)")
mycursor.execute("CREATE TABLE `users` (`ID` TEXT NOT NULL,`C1` TEXT NOT NULL,`C2` TEXT NOT NULL,`C3` TEXT NOT NULL,`C4` TEXT NOT NULL,`C5` TEXT NOT NULL)")

DB.ChallengesDB.commit()


mycursor = DB.EventDB.cursor()

mycursor.execute("DROP TABLE IF EXISTS events")
mycursor.execute("DROP TABLE IF EXISTS users")

mycursor.execute("CREATE TABLE `events` (`ID` TEXT NOT NULL,`Name` TEXT NOT NULL,`Type` TEXT NOT NULL,`A` TEXT NOT NULL,`B` TEXT NOT NULL,`Op` TEXT NOT NULL,`Data` TEXT NOT NULL)")
mycursor.execute("CREATE TABLE `users` (`UID` TEXT NOT NULL,`EID` TEXT NOT NULL,`Date` INT NOT NULL)")

DB.EventDB.commit()


mycursor = DB.RewardsDB.cursor()

mycursor.execute("DROP TABLE IF EXISTS lotto")
mycursor.execute("DROP TABLE IF EXISTS codes")
mycursor.execute("DROP TABLE IF EXISTS creators")

mycursor.execute("CREATE TABLE `lotto` (`ID` TEXT NOT NULL,`Type` TEXT NOT NULL,`Numbers` TEXT NOT NULL,`Reward` TEXT NOT NULL,`Date` TEXT NOT NULL)")
mycursor.execute("CREATE TABLE `codes` (`Code` TEXT NOT NULL,`EID` TEXT NOT NULL,`DateInvalid` TEXT NOT NULL)")
mycursor.execute("CREATE TABLE `creators` (`UID` TEXT NOT NULL,`Code` TEXT NOT NULL,`Name` TEXT NOT NULL,`Date` TEXT NOT NULL)")

DB.RewardsDB.commit()