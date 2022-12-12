from __main__ import app

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB


@app.route("/applyadmin", methods=["POST", "GET"])
def ApplyForAdmin():
    return render_template("admin/applyadmin.html")


@app.route("/applyadminp", methods=["POST", "GET"])
def PostApplyForAdmin():
    if Data.ValidateID(request.form["uid"]) and Data.ValidateUser(request.form["fname"], hashlib.sha512(request.form["pwd"].encode()).hexdigest()):
        f = open(
            "data/applications/"
            + request.form["fname"]
            + "-"
            + request.form["uid"]
            + ".txt",
            "w",
        )
        f.write(request.form["uid"] + "\n")
        f.write(request.form["fname"] + "\n")
        f.write(hashlib.sha512(request.form["pwd"].encode()).hexdigest() + "\n")
        f.write(
            [
                "I want to help make it a better place",
                "I want to bully people",
                "I want to help improve the platform",
            ][int(request.form["whyradio"])]
            + "\n"
        )
        f.write(request.form["whyother"] + "\n")
        f.close()
        return redirect(url_for("HomePage"))
    else:
        return redirect(url_for("SignIn"))