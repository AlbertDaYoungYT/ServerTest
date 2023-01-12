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

staticTextPage["about"] = {}
staticTextPage["about"]["default"] = {}

staticTextPage["error404"] = {}




staticTextPage["header"]["LeftPageNames"] = ["Home", "Games", "Shop", "About"]
staticTextPage["header"]["RightPageNames"] = ["Login", "Signup"]

staticTextPage["header"]["ProMenuDropDown"] = [
    "Friends",
    "Trades",
    "Challenges",
    "Shop Transactions",
    "Inventory",
    "Admin Panel",
    "Profile",
    "Sign Out"
]

staticTextPage["header"]["Notifi1"] = "Notifications"
staticTextPage["header"]["NoNotifi1"] = "No Notifications"

staticTextPage["header"]["NotifiButton1"] = "Accept"
staticTextPage["header"]["NotifiButton2"] = "Deny"


staticTextPage["footer"]["Tabel1"] = [
    "Site",
    [
        "Home",
        "Games",
        "Shop",
        "About"
    ],
    "Profile"
]
staticTextPage["footer"]["Tabel2"] = [
    "Help",
    [
        "How to Play",
        "Help Center"
    ]
]
staticTextPage["footer"]["Tabel3"] = [
    "Me",
    [
        "About",
        "Profile",
        "Donate",
        "Ask The Creator",
        "Pitch an Idea"
    ]
]
staticTextPage["footer"]["Subscribe"] = [
    "Subscribe to our Rewards Program",
    "Get Challenges in your inbox to earn ingame Credits",
    "Email address",
    "Subscribe"
]

staticTextPage["home"]["default"]["Title"]               = "Home - Web Realms"
staticTextPage["home"]["newuser"]["Text1"]               = "SiteText1"
staticTextPage["home"]["newuser"]["Text2"]               = "SiteText2"
staticTextPage["home"]["newuser"]["Button1"]             = ["Signup", "/signup"]
staticTextPage["home"]["newuser"]["Button2"]             = ["Login", "/signin"]
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
staticTextPage["signin"]["default"]["Text1"]             = "Please signin"
staticTextPage["signin"]["default"]["Form1"]             = "Username"
staticTextPage["signin"]["default"]["Form2"]             = "Password"
staticTextPage["signin"]["default"]["Button1"]           = "Signin"
staticTextPage["signin"]["default"]["Button2"]           = "Home"

staticTextPage["shop"]["newuser"]["Title"]               = "Shop - Web Realms"
staticTextPage["shop"]["newuser"]["Name1"]               = "Welcome to the Shop"
staticTextPage["shop"]["newuser"]["Name2"]               = "Welcome to the Market"
staticTextPage["shop"]["newuser"]["Text1"]               = "SiteText1"
staticTextPage["shop"]["newuser"]["Text2"]               = "SiteText2"
staticTextPage["shop"]["newuser"]["Button1"]             = ["Go to Shop", "#shop"]
staticTextPage["shop"]["newuser"]["Button2"]             = ["Go to Market", "#market"]

staticTextPage["ask"]["default"]["Title"]               = "Ask The Creator - Web Realms"
staticTextPage["ask"]["default"]["Text1"]               = "Welcome to Ask The Creator"
staticTextPage["ask"]["default"]["Text2"]               = "The place where you can ask the creator, AKA Me questions about anything and i will try my best to answer them"

staticTextPage["about"]["default"]["Title"]               = "About - Web Realms"
staticTextPage["about"]["default"]["Text1"]               = "Welcome to Ask The Creator"
staticTextPage["about"]["default"]["Text2"]               = "The place where you can ask the creator, AKA Me questions about anything and i will try my best to answer them"

staticTextPage["error404"]["Title"] = "Error 404"
staticTextPage["error404"]["ErrorCode"] = "404"
staticTextPage["error404"]["BoldText"] = "Opps!"
staticTextPage["error404"]["Text1"] = "Page not found."
staticTextPage["error404"]["Text2"] = "The page you're looking for doesn't exist."
staticTextPage["error404"]["Button1"] = "Go Home"
