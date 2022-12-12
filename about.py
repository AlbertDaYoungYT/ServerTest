from __main__ import app

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB


@app.route("/about")
def About():
    return render_template(
        "about.html",
        content=Text.aboutTextPage,
        UserProfileSrc="Test",
        UserName="Test",
        UserProfile="Test",
        isloggedin=True,
        isadmin=False,
    )