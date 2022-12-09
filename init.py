import db as DB

mycursor = DB.db.cursor()

mycursor.execute("DROP TABLE users")
mycursor.execute("DROP TABLE themes")
mycursor.execute("DROP TABLE userdata")
mycursor.execute("CREATE TABLE `users` (`ID` TEXT NOT NULL,`Username` TEXT NOT NULL,`PwdHash` TEXT NOT NULL,`CreationDate` INT NOT NULL)")
mycursor.execute("CREATE TABLE `userdata` (`ID` TEXT NOT NULL,`DisplayName` TEXT NOT NULL,`ProfileIMG` INT NOT NULL,`isadmin` TEXT NOT NULL)")
mycursor.execute("CREATE TABLE `themes` (`Name` TEXT NOT NULL,`color1` TEXT NOT NULL,`color2` INT NOT NULL,`color3` TEXT NOT NULL,`color4` TEXT NOT NULL,`color5` TEXT NOT NULL)")

mycursor.execute("INSERT INTO themes (Name, color1, color2, color3, color4, color5) VALUES ('default', '#0d1821', '#f0f4ef', '#9c0d38', '#05001e', '#b370b0')")

DB.db.commit()
