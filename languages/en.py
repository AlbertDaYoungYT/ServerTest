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




staticTextPage["header"]["Page1"] = "Home"
staticTextPage["header"]["Page2"] = "Games"
staticTextPage["header"]["Page3"] = "Shop"
staticTextPage["header"]["Page4"] = "About"

staticTextPage["footer"]["default"] = "Home"
staticTextPage["footer"]["default"] = "Shop"
staticTextPage["footer"]["default"] = "Leaderboard"
staticTextPage["footer"]["default"] = "About"

staticTextPage["home"]["default"]["Title"]               = "Home - Web Realms"
staticTextPage["home"]["newuser"]["Text1"]               = "SiteText1"
staticTextPage["home"]["newuser"]["Text2"]               = "SiteText2"
staticTextPage["home"]["newuser"]["Button1"]          = ["Signup", "/signup"]
staticTextPage["home"]["newuser"]["Button2"]          = ["Login", "/signin"]
staticTextPage["home"]['newuser']['Welcome']             = "Welcome to"
staticTextPage["home"]["logedin"]["Welcome"]             = [
    "Welcome back to your online home %s!",
    "Welcome back to our community %s!",
    "Glad to have you back with us %s!",
    "Hi there and welcome back %s!",
    "Welcome back to our site %s!",
    "Hello and welcome back %s!",
    "Hello %s and welcome back!",
    "Glad to have you back %s!",
    "Glad to see you again %s!",
    "Hi and welcome back %s!",
    "Welcome back %s!"
]

staticTextPage["home"]["newuser"]["ColumnName"]           = "ColumnName"
staticTextPage["home"]["newuser"]["ColumnCount"]          = 3
staticTextPage["home"]["newuser"]["ColumnIcons"]          = ["/static/favicons/close.png", "/static/favicons/close.png", "/static/favicons/close.png"]
staticTextPage["home"]["newuser"]["ColumnTitles"]         = ["ColumnTitles", "ColumnTitles", "ColumnTitles"]
staticTextPage["home"]["newuser"]["ColumnDiscriptions"]   = ["ColumnDiscriptions", "ColumnDiscriptions", "ColumnDiscriptions"]
staticTextPage["home"]["newuser"]["ColumnLinks"]          = ["/", "/", "/"]
staticTextPage["home"]["newuser"]["ColumnLinkNames"]      = ["ColumnLinkNames", "ColumnLinkNames", "ColumnLinkNames"]

staticTextPage["signup"]["default"]["Title"]             = "Sign Up - Web Realms"
staticTextPage["signup"]["default"]["Text1"]             = "SiteText1"
staticTextPage["signup"]["default"]["Text2"]             = "SiteText2"

staticTextPage["signin"]["default"]["Title"]             = "Sign In - Web Realms"
staticTextPage["signin"]["default"]["Text1"]             = "SiteText1"
staticTextPage["signin"]["default"]["Text2"]             = "SiteText2"

staticTextPage["shop"]["newuser"]["Title"]               = "Shop - Web Realms"
staticTextPage["shop"]["newuser"]["Text1"]               = "SiteText1"
staticTextPage["shop"]["newuser"]["Text2"]               = "SiteText2"
staticTextPage["shop"]["newuser"]["Button1"]             = ["Go to Shop", "#shop"]
staticTextPage["shop"]["newuser"]["Button2"]             = ["Go to Market", "#market"]

staticTextPage["ask"]["default"]["Title"]               = "Ask The Creator - Web Realms"
staticTextPage["ask"]["default"]["Text1"]               = "Welcome to Ask The Creator"
staticTextPage["ask"]["default"]["Text2"]               = "The place where you can ask the creator, AKA Me questions about anything and i will try my best to answer them"