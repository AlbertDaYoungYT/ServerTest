import db as DB

mycursor = DB.db.cursor()

mycursor.execute("DROP TABLE cookies")
mycursor.execute("CREATE TABLE `cookies` (`cookieid` TEXT(64) NOT NULL, `expires` INT NOT NULL);")

DB.db.commit()