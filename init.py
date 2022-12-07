import db as DB

mycursor = DB.db.cursor()

mycursor.execute("DROP TABLE users")
mycursor.execute("CREATE TABLE `users` (`ID` TEXT NOT NULL,`Username` TEXT NOT NULL,`PwdHash` TEXT NOT NULL,`CreationDate` INT NOT NULL)")

DB.db.commit()