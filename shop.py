from __main__ import *

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB


@app.route("/shop")
def Shop():
    return render_template(
        "shop.html",
        content=Text.ShopItems,
        UserProfileSrc="Test",
        UserName="Test",
        UserProfile="Test",
        isloggedin=True,
        isadmin=False,
    )