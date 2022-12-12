from __main__ import *

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB


@app.route("/confirmsignin", methods=["POST"])
def ConfirmLogin():
    if Data.ValidateUser(
        request.form["user"], hashlib.sha512(request.form["pwd"].encode()).hexdigest()
    ):
        Uid = Data.FetchUID(
            request.form["user"],
            hashlib.sha512(request.form["pwd"].encode()).hexdigest(),
        )
        if Uid != False:
            session["Uid"] = Uid
            return redirect(url_for("HomePage"))
        else:
            flash("Uid could not be found, please contact an admin")
            return redirect(url_for("SignIn"))

    flash("Incorrect Username or Password")
    return redirect(url_for("SignIn"))


@app.route("/signin")
def SignIn():
    return render_template("login.html")