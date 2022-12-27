import base64
from flask import *
from werkzeug.utils import *
from flask_cors import CORS
from datetime import *
import hashlib
import uuid
import os

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.BadgeDB as BD
import modules.Theme as T
import data.settings as S
import db as DB

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "static/favicons/uploads"

app.secret_key = S.SECRET
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


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


@app.route("/admin")
def AdminURL():
    return redirect(url_for("AdminHome"))


@app.route("/admin/homepage")
def AdminHome():
    Uid = session.get("Uid")
    if Uid == None:
        return redirect(url_for("HomePage"))
    else:
        data = list(UP.FetchUserdata(Uid))
        edata = list(UP.FetchEUserdata(Uid))
        try:
            if "".join(data) == "NOTFOUND":
                return redirect(url_for("LogOut"))
        except Exception as e:
            pass

        try:
            Theme = session["theme"]
        except Exception as e:
            Theme = "default"
        Theme = T.FetchTheme(Theme)

        if data[-1] == "False":
            admin = False
        else:
            admin = True

        return render_template(
            "admin/index.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            Description=data[3],
            isloggedin=True,
            isadmin=admin,
            Fullname=edata[4],
            Email=edata[3],
            Phone=edata[2],
            Address=edata[1],
            color1=Theme[1],
            color2=Theme[2],
            color3=Theme[3],
            color4=Theme[4],
            color5=Theme[5],
        )


@app.route("/applyadmin")
def ApplyForAdmin():
    return render_template("admin/applyadmin.html")


@app.route("/applyadminp", methods=["POST", "GET"])
def PostApplyForAdmin():
    if Data.ValidateID(request.form["uid"]) and Data.ValidateUser(
        request.form["fname"], hashlib.sha512(request.form["pwd"].encode()).hexdigest()
    ):
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


@app.route("/")
def HomePage():
    Uid = session.get("Uid")
    if Uid == None:
        Theme = T.FetchDefaultTheme()
        return render_template(
            "index.html",
            UserProfileSrc="Test",
            UserName="Test",
            UserProfile="Test",
            isloggedin=False,
            isadmin=False,
            color1=Theme[1],
            color2=Theme[2],
            color3=Theme[3],
            color4=Theme[4],
            color5=Theme[5],
        )
    else:
        data = list(UP.FetchUserdata(Uid))
        badges = [BD.FetchBadge(badge[1]) for badge in list(BD.FetchUserBadges(Uid))]
        try:
            if "".join(data) == "NOTFOUND":
                return redirect(url_for("LogOut"))
        except Exception as e:
            pass

        try:
            Theme = session["theme"]
        except Exception as e:
            Theme = "default"
        Theme = T.FetchTheme(Theme)

        if data[-1] == "False":
            admin = False
        else:
            admin = True

        return render_template(
            "index.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            isloggedin=True,
            isadmin=admin,
            Badges=badges,
            color1=Theme[1],
            color2=Theme[2],
            color3=Theme[3],
            color4=Theme[4],
            color5=Theme[5],
        )


@app.route("/profile/<uid>")
def ProfileURL(uid):
    try:
        if uid == str(session["Uid"]):
            data = list(UP.FetchUserdata(uid))
            edata = list(UP.FetchEUserdata(uid))
            try:
                if "".join(data) == "NOTFOUND":
                    return redirect(url_for("LogOut"))
            except Exception as e:
                pass

            try:
                Theme = session["theme"]
            except Exception as e:
                Theme = "default"
            Theme = T.FetchTheme(Theme)

            if data[-1] == "False":
                admin = False
            else:
                admin = True

            return render_template(
                "profile/profile.html",
                Uid=data[0],
                UserProfileSrc=f"/static/favicons/{data[2]}",
                UserName=data[1],
                UserProfile=f"{data[0]}",
                Description=data[3],
                isloggedin=True,
                isadmin=admin,
                Fullname=edata[4],
                Email=edata[3],
                Phone=edata[2],
                Address=edata[1],
                color1=Theme[1],
                color2=Theme[2],
                color3=Theme[3],
                color4=Theme[4],
                color5=Theme[5],
            )
    except Exception as e:
        pass

    return redirect(url_for("HomePage"))


@app.route("/profile/<uid>/edit")
def EditProfile(uid):
    try:
        if uid == str(session["Uid"]):
            data = list(UP.FetchUserdata(uid))
            edata = list(UP.FetchEUserdata(uid))
            try:
                if "".join(data) == "NOTFOUND":
                    return redirect(url_for("LogOut"))
            except Exception as e:
                pass

            try:
                Theme = session["theme"]
            except Exception as e:
                Theme = "default"
            Theme = T.FetchTheme(Theme)

            if data[-1] == "False":
                admin = False
            else:
                admin = True

            return render_template(
                "profile/edit.html",
                Uid=data[0],
                UserProfileSrc=f"/static/favicons/{data[2]}",
                UserName=data[1],
                UserProfile=f"{data[0]}",
                Description=data[3],
                isloggedin=True,
                isadmin=admin,
                Fullname=edata[4],
                Email=edata[3],
                Phone=edata[2],
                Address=edata[1],
                color1=Theme[1],
                color2=Theme[2],
                color3=Theme[3],
                color4=Theme[4],
                color5=Theme[5],
            )
    except Exception as e:
        pass

    return redirect(url_for("ProfileURL", uid=data[0]))


@app.route("/profile/<uid>/postedit", methods=["POST"])
def PostEditProfile(uid):
    if uid == str(session["Uid"]):
        try:
            if "" in request.form.keys():
                flash("Error: No Inputs")
                return redirect(url_for("ProfileURL", uid=str(session["Uid"])))
            else:
                UP.UpdateUserdata(
                    uid,
                    request.form["adr"],
                    request.form["email"],
                    request.form["phone"],
                    request.form["fname"],
                    request.form["dname"],
                    request.form["disc"],
                )
                return redirect(url_for("ProfileURL", uid=str(session["Uid"])))
        except Exception as e:
            flash(str(e))
            return redirect(url_for("ProfileURL", uid=str(session["Uid"])))
    else:
        return redirect(url_for("HomePage"))


@app.route("/profile/<uid>/badges")
def ProfileBadgeList(uid):
    if uid == str(session["Uid"]):
        data = list(UP.FetchUserdata(uid))
        badges = [BD.FetchBadge(badge[1]) for badge in list(BD.FetchUserBadges(uid))]
        badges = [
            badge + [BD.CalculateRarity(BD.FetchBadge(badge[0])[4])] for badge in badges
        ]
        badges.sort(key=lambda x: x[-1])
        try:
            if "".join(data) == "NOTFOUND":
                return redirect(url_for("LogOut"))
        except Exception as e:
            pass

        try:
            Theme = session["theme"]
        except Exception as e:
            Theme = "default"
        Theme = T.FetchTheme(Theme)

        if data[-1] == "False":
            admin = False
        else:
            admin = True

        return render_template(
            "profile/badge.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            isloggedin=True,
            isadmin=admin,
            Badges=badges,
            BadgeTime=badgeTime,
            len=len(badgeTime),
            BadgeRanks=S.RARITY_RANKS,
            color1=Theme[1],
            color2=Theme[2],
            color3=Theme[3],
            color4=Theme[4],
            color5=Theme[5],
        )
    else:
        return redirect(url_for("HomePage"))


@app.route("/addfriend/<uid>")
def AddFriend(uid):
    return ""


@app.route("/profile/<uid>/badges/<urlbadgeid>")
def ProfileBadge(uid, urlbadgeid):
    if uid == str(session["Uid"]):
        data = list(UP.FetchUserdata(uid))
        badge = BD.FetchBadge(base64.urlsafe_b64decode(urlbadgeid).decode())
        rarity = BD.CalculateRarity(badge[4], normal=False)

        try:
            if "".join(data) == "NOTFOUND":
                return redirect(url_for("LogOut"))
        except Exception as e:
            pass

        try:
            Theme = session["theme"]
        except Exception as e:
            Theme = "default"
        Theme = T.FetchTheme(Theme)

        if data[-1] == "False":
            admin = False
        else:
            admin = True
        
        badgeTime = datetime.fromtimestamp(round(badge[6]))

        return render_template(
            "profile/specific-badge.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            isloggedin=True,
            isadmin=admin,
            badge=badge,
            badgeRarity=rarity,
            badgeTime=badgeTime,
            color1=Theme[1],
            color2=Theme[2],
            color3=Theme[3],
            color4=Theme[4],
            color5=Theme[5],
        )
    else:
        return redirect(url_for("HomePage"))


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
        except Exception as e:
            print(e)
            flash("Some fields are not filled out correctly")
            return redirect(url_for("SignUp"))

    flash("User already exists")
    return redirect(url_for("SignUp"))


@app.route("/signup")
def SignUp():
    return render_template("signup.html")


@app.route("/logout")
def LogOut():
    session.clear()
    return redirect(url_for("HomePage"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, debug=True, ssl_context=("cert.pem", "key.pem"))
