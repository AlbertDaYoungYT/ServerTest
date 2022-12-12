from __main__ import *

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB

app.route("/admin")
def Admin():
    return redirect(url_for("AdminHome"))

app.route("/admin/home")
def AdminHome():
    return render_template("admin/index.html")