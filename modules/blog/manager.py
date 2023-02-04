import modules.time as time

def PostBlog(ID, DisplayName, Username, PwdHash, bday):
    cursor = BlogDB.cursor()
    cursor.execute(f"INSERT INTO users (ID, Username, PwdHash, CreationDate) VALUES ('{ID}', '{Username}', '{PwdHash}', '{time.utime()}')")
    cursor.execute(f"INSERT INTO userdata (ID, DisplayName, ProfileIMG, Description, Birthday, GCoins, Credits, isadmin) VALUES ('{ID}', '{DisplayName}', 'default.png', '', '{bday}', 0, 0, 'False')")
    cursor.execute(f"INSERT INTO euserdata (ID, Address, Email, Phone, Fullname) VALUES ('{ID}', '', '', '', '')")

    BlogDB.commit()

def FetchBlog(Time):
    cursor = BlogDB.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    for result in results:
        result = list(result)
        if result[1] == Username and result[2] == PwdHash:
            return result[0]
    
    return False
