global staticTextPage
staticTextPage = {}
staticTextPage["header"] = {}
staticTextPage["footer"] = {}
staticTextPage["home"] = {}
staticTextPage["home"]["default"] = {}
staticTextPage["home"]["newuser"] = {}
staticTextPage["home"]["logedin"] = {}

staticTextPage["signup"] = {}
staticTextPage["signup"]["default"] = {}

staticTextPage["signin"] = {}
staticTextPage["signin"]["default"] = {}

staticTextPage["shop"] = {}
staticTextPage["shop"]["default"] = {}
staticTextPage["shop"]["newuser"] = {}
staticTextPage["shop"]["logedin"] = {}

staticTextPage["ask"] = {}
staticTextPage["ask"]["default"] = {}
staticTextPage["ask"]["newuser"] = {}
staticTextPage["ask"]["logedin"] = {}




staticTextPage["header"]["Page1"] = "Hjem"
staticTextPage["header"]["Page2"] = "Spil"
staticTextPage["header"]["Page3"] = "Butik"
staticTextPage["header"]["Page4"] = "Om"

staticTextPage["home"]["default"]["Title"] = "Hjem - Web Realms"
staticTextPage["home"]["newuser"]["Text1"] = "Text1"
staticTextPage["home"]["newuser"]["Text2"] = "Text2"
staticTextPage["home"]["newuser"]["Button1"] = ["Tilmeld", "/signup"]
staticTextPage["home"]["newuser"]["Button2"] = ["Logind", "/signin"]
staticTextPage["home"]['newuser']['Welcome']             = "Velkommen til"
staticTextPage["home"]["logedin"]["Welcome"] = [
    "Vi håber, du vil føle dig hjemme her %s",
    "Det er en fornøjelse at have dig %s",
    "Vi er beærede over at have dig %s.",
    "Velkommen til dit online hjem %s",
    "Vi glæder os til at møde dig %s!",
    "Tillykke med at finde vej %s!",
    "Velkommen til vores hjem %s.",
    "Så glad for at du er her %s!",
    "Tak fordi du besøger os %s.",
    "Velkommen tilbage %s!"
]
staticTextPage["home"]["newuser"]["ColumnName"]           = "ColumnName"
staticTextPage["home"]["newuser"]["ColumnCount"]          = 3
staticTextPage["home"]["newuser"]["ColumnIcons"]          = ["/static/favicons/close.png", "/static/favicons/close.png", "/static/favicons/close.png"]
staticTextPage["home"]["newuser"]["ColumnTitles"]         = ["ColumnTitles", "ColumnTitles", "ColumnTitles"]
staticTextPage["home"]["newuser"]["ColumnDiscriptions"]   = ["ColumnDiscriptions", "ColumnDiscriptions", "ColumnDiscriptions"]
staticTextPage["home"]["newuser"]["ColumnLinks"]          = ["/", "/", "/"]
staticTextPage["home"]["newuser"]["ColumnLinkNames"]      = ["ColumnLinkNames", "ColumnLinkNames", "ColumnLinkNames"]

staticTextPage["signup"]["default"]["Title"]             = "Tilmeld - Web Realms"
staticTextPage["signup"]["default"]["Text1"]             = "SiteText1"
staticTextPage["signup"]["default"]["Text2"]             = "SiteText2"

staticTextPage["signin"]["default"]["Title"]             = "Logind - Web Realms"
staticTextPage["signin"]["default"]["Text1"]             = "SiteText1"
staticTextPage["signin"]["default"]["Text2"]             = "SiteText2"

staticTextPage["shop"]["newuser"]["Title"]               = "Butik - Web Realms"
staticTextPage["shop"]["newuser"]["Text1"]               = "SiteText1"
staticTextPage["shop"]["newuser"]["Text2"]               = "SiteText2"
staticTextPage["shop"]["newuser"]["Button1"]             = ["Gå til Butikken", "#shop"]
staticTextPage["shop"]["newuser"]["Button2"]             = ["Gå til Marked", "#market"]

staticTextPage["ask"]["default"]["Title"]               = "Spørg Skaberen - Web Realms"
staticTextPage["ask"]["default"]["Text1"]               = "Velkommen til Spørg Skaberen"
staticTextPage["ask"]["default"]["Text2"]               = "Stedet, hvor du kan stille skaberen, AKA Mig spørgsmål om hvad som helst, og jeg vil gøre mit bedste for at besvare spørgsmålet"