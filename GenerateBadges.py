import modules.BadgeEncryptionAlgo as BEA
import modules.BadgeDB as BD
import db as DB

mycursor = DB.MainDB.cursor()

mycursor.execute("DROP TABLE IF EXISTS badges")
mycursor.execute("DROP TABLE IF EXISTS badgeowners")
mycursor.execute("CREATE TABLE `badges` (`BadgeID` TEXT NOT NULL,`UrlBadgeID` TEXT NOT NULL,`Name` TEXT NOT NULL,`Description` TEXT NOT NULL,`Type` TEXT NOT NULL,`ImageURL` TEXT NOT NULL,`CreationDate` INT NOT NULL)")
mycursor.execute("CREATE TABLE `badgeowners` (`OwnerID` TEXT NOT NULL,`BadgeID` TEXT NOT NULL,`achievementDate` INT NOT NULL)")

DB.MainDB.commit()

for x in range(10):
    BID = BD.CreateBadge(f"b{x}", f"be b{x}", "test", "trophy.png")
    BD.SetBadgeToUser(BID, "d7e90f11-8943-11ed-90d9-001a7dda7111")
    print(BID)

BID = BD.CreateBadge(f"b{x}", f"be b{x}", "damn", "trophy.png")
BD.SetBadgeToUser(BID, "d7e90f11-8943-11ed-90d9-001a7dda7111")
BID = BD.CreateBadge(f"b{x}", f"be b{x}", "damn", "trophy.png")
BD.SetBadgeToUser(BID, "d7e90f11-8943-11ed-90d9-001a7dda7111")