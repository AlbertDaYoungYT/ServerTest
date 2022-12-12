from __main__ import *

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB


@app.route("/confirmsignup", methods=["POST"])
def ConfirmSignup():
    if not Data.ValidateUser(
        request.form["user"], hashlib.sha512(request.form["pwd"].encode()).hexdigest()
    ):
        try:
            if (
                len(request.form["bday"]) == 10
                and len(request.form["bday"].split("-")) == 3
            ):
                Uid = uuid.uuid1()
                session["Uid"] = Uid
                session["theme"] = "default"
                Data.CreateUser(
                    Uid,
                    request.form["dname"],
                    request.form["user"],
                    hashlib.sha512(request.form["pwd"].encode()).hexdigest(),
                    request.form["bday"],
                )

                return redirect(url_for("HomePage"))
        except Exception:
            flash("Some fields are not filled out correctly")
            return redirect(url_for("SignUp"))

    flash("User already exists")
    return redirect(url_for("SignUp"))


@app.route("/signup")
def SignUp():
    return render_template("signup.html")