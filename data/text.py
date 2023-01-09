global staticPageData
staticPageData = {}

staticPageData["SiteName"]             = "Web Realms"
staticPageData["CompanyName"]          = "RealmTech Games"
staticPageData["CompanyTwitter"]       = "https://youtu.be/dQw4w9WgXcQ&autoplay=1"
staticPageData["CompanyInstagram"]     = "https://youtu.be/dQw4w9WgXcQ&autoplay=1"
staticPageData["CompanyYoutube"]       = "https://youtu.be/dQw4w9WgXcQ&autoplay=1"







import languages.en
import languages.da



def LoadLanguagePage(page, language="en"):
    if   language == "en":
        text = languages.en.staticTextPage[page.lower()] + languages.en.staticTextPage["header"] + languages.en.staticTextPage["footer"]
    elif language == "da":
        text = languages.da.staticTextPage[page.lower()] + languages.da.staticTextPage["header"] + languages.da.staticTextPage["footer"]
    else:
        text = None

    return text