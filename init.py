import db as DB

mycursor = DB.db.cursor()

mycursor.execute("DROP TABLE users")
mycursor.execute("DROP TABLE userdata")
mycursor.execute("CREATE TABLE `users` (`ID` TEXT NOT NULL,`Username` TEXT NOT NULL,`PwdHash` TEXT NOT NULL,`CreationDate` INT NOT NULL)")
mycursor.execute("CREATE TABLE `userdata` (`ID` TEXT NOT NULL,`DisplayName` TEXT NOT NULL,`ProfileIMG` INT NOT NULL,`isadmin` TEXT NOT NULL)")

DB.db.commit()