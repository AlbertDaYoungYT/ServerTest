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

staticTextPage["error404"] = {}




staticTextPage["header"]["PageNames"] = ["Hjem", "Spil", "Butik", "Om"]

staticTextPage["header"]["ProMenuDropDown"] = [
    "Venner",
    "Handel",
    "Udfordringer",
    "Butikstransaktioner",
    "Inventar",
    "Admin Panel",
    "Profil",
    "Log ud"
]

staticTextPage["header"]["Notifi1"] = "Meddelelser"
staticTextPage["header"]["NoNotifi1"] = "Ingen Meddelelser"

staticTextPage["header"]["NotifiButton1"] = "Acceptere"
staticTextPage["header"]["NotifiButton2"] = "Afvis"


staticTextPage["footer"]["Tabel1"] = [
    "Websted",
    [
        "Hjem",
        "Spil",
        "Butik",
        "Om"
    ],
    "Profil"
]
staticTextPage["footer"]["Tabel2"] = [
    "Hjælp",
    [
        "Hvordan Spiller man",
        "Hjælpe Center"
    ]
]
staticTextPage["footer"]["Tabel3"] = [
    "Mig",
    [
        "Om",
        "Profil",
        "Doner",
        "Spørg Skaberen",
        "Pitch en Idé"
    ]
]
staticTextPage["footer"]["Subscribe"] = [
    "Abonner på vores Belønningsprogram",
    "Få udfordringer i din indbakke for at optjene ingame-kreditter",
    "Email adresse",
    "Abonner"
]

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
staticTextPage["signin"]["default"]["Text1"]             = "Log venligst på"
staticTextPage["signin"]["default"]["Form1"]             = "Brugernavn"
staticTextPage["signin"]["default"]["Form2"]             = "Adgangskode"
staticTextPage["signin"]["default"]["Button1"]           = "Logind"
staticTextPage["signin"]["default"]["Button2"]           = "Hjem"

staticTextPage["shop"]["newuser"]["Title"]               = "Butik - Web Realms"
staticTextPage["shop"]["newuser"]["Name1"]               = "Velkommen til Butikken"
staticTextPage["shop"]["newuser"]["Name2"]               = "Velkommen til Marked"
staticTextPage["shop"]["newuser"]["Text1"]               = "SiteText1"
staticTextPage["shop"]["newuser"]["Text2"]               = "SiteText2"
staticTextPage["shop"]["newuser"]["Button1"]             = ["Gå til Butikken", "#shop"]
staticTextPage["shop"]["newuser"]["Button2"]             = ["Gå til Marked", "#market"]

staticTextPage["ask"]["default"]["Title"]               = "Spørg Skaberen - Web Realms"
staticTextPage["ask"]["default"]["Text1"]               = "Velkommen til Spørg Skaberen"
staticTextPage["ask"]["default"]["Text2"]               = "Stedet, hvor du kan stille skaberen, AKA Mig spørgsmål om hvad som helst, og jeg vil gøre mit bedste for at besvare spørgsmålet"

staticTextPage["error404"]["Title"] = "Error 404"
staticTextPage["error404"]["ErrorCode"] = "404"
staticTextPage["error404"]["BoldText"] = "Opps!"
staticTextPage["error404"]["Text1"] = "Siden blev ikke fundet."
staticTextPage["error404"]["Text2"] = "Siden du leder efter findes ikke."
staticTextPage["error404"]["Button1"] = "Gå Hjem"