global staticPageData
staticPageData = {}

staticPageData["SiteName"]             = "Web Realms"
staticPageData["CompanyName"]          = "RealmTech Games"
staticPageData["CompanyTwitter"]       = "https://youtu.be/dQw4w9WgXcQ&autoplay=1"
staticPageData["CompanyInstagram"]     = "https://youtu.be/dQw4w9WgXcQ&autoplay=1"
staticPageData["CompanyYoutube"]       = "https://youtu.be/dQw4w9WgXcQ&autoplay=1"

staticPageData["FooterTabelLink1"] = []
staticPageData["FooterTabelLink2"] = []
staticPageData["FooterTabelLink3"] = []

staticPageData["HeaderNavLinks"] = ["/", "/games", "/shop", "/about"]
staticPageData["HeaderNavCount"] = len(staticPageData["HeaderNavLinks"])
staticPageData["HeaderProLinks"] = [
    {
        "Name": "Friends",
        "Link": ["/profile/", "/friendlist"]
    }
]







import languages.en
import languages.da



def LoadLanguagePage(page, language="en"):
    if   language == "en":
        text = languages.en.staticTextPage[page.lower()].copy()
        text.update(languages.en.staticTextPage["header"])
        text.update(languages.en.staticTextPage["footer"])
    elif language == "da":
        text = languages.da.staticTextPage[page.lower()].copy()
        text.update(languages.da.staticTextPage["header"])
        text.update(languages.da.staticTextPage["footer"])
    else:
        text = None

    print(text)
    return text