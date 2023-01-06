from __future__ import division

import base64
from flask import *
from werkzeug.utils import *
from flask_cors import CORS
from datetime import datetime, timedelta, date
import hashlib
import random
import uuid
import html
import os
import re

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.notifications as N
import modules.Email as E
import modules.friends as F
import modules.BadgeDB as BD
import modules.Theme as T
import modules.time as time
import data.settings as S
import db as DB

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "static/favicons/uploads"
EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

app.secret_key = S.SECRET
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


def check_email(email):
    if re.fullmatch(EMAIL_REGEX, email):
        return True
    else:
        return False


def seconds_to_hhmmss(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def calculate_notifier_times(Notifiers):
    NotifierTimes = [x[-1] for x in Notifiers]
    NotifierTimesDiff = [time.time() - x for x in NotifierTimes]
    NotifierTimesDiffText = [seconds_to_hhmmss(x) for x in NotifierTimesDiff]

    x = []
    for Notifier in range(len(Notifiers)):
        n = [int(x) for x in NotifierTimesDiffText[Notifier].split(":")]
        if n[2] > 0 and n[1] < 1:
            x.append(str(n[2]) + " Seconds Ago")
        elif n[1] > 0 and n[0] < 1:
            x.append(str(n[1] + round(n[2] / 100)) + " Minutes Ago")
        elif n[0] > 0:
            x.append(str(n[0] + round(n[1] / 100)) + " Hours Ago")
        else:
            x.append(str(time.todate(NotifierTimes[Notifier])).split()[0])

    final = []
    for Notifier in range(len(Notifiers)):
        final.append(Notifiers[Notifier][0:-1] + [x[Notifier]])

    return final














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
            SiteData=Text.homeTextPage,
            StaticData=Text.staticPageData,
            isloggedin=False,
            isadmin=False,
            Theme=Theme,
            Page="Home",
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

        Notifications = N.friend.FetchNotifiers(Uid)
        NoNotifiers = False
        if Notifications == []:
            NoNotifiers = True

        Notifications = calculate_notifier_times(Notifications)

        return render_template(
            "index.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            SiteData=Text.homeTextPage,
            StaticData=Text.staticPageData,
            SiteWelcome=random.choice(Text.homeTextPage["SiteWelcome"]) % (data[1],),
            isloggedin=True,
            isadmin=False,
            Theme=Theme,
            Page="Home",
            Badges=badges,
            Notifications=[[html.unescape(str(y)) for y in x] for x in Notifications],
            noNotifiers=NoNotifiers,
        )


@app.route("/about")
def About():
    Uid = session.get("Uid")
    if Uid == None:
        Theme = T.FetchDefaultTheme()
        return render_template(
            "about.html",
            UserProfileSrc="Test",
            UserName="Test",
            UserProfile="Test",
            SiteData=Text.aboutTextPage,
            StaticData=Text.staticPageData,
            isloggedin=False,
            isadmin=False,
            Theme=Theme,
            Page="About",
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

        Notifications = N.friend.FetchNotifiers(Uid)
        NoNotifiers = False
        if Notifications == []:
            NoNotifiers = True

        Notifications = calculate_notifier_times(Notifications)

        return render_template(
            "about.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            SiteData=Text.aboutTextPage,
            StaticData=Text.staticPageData,
            SiteWelcome=random.choice(Text.homeTextPage["SiteWelcome"]) % (data[1],),
            isloggedin=True,
            isadmin=False,
            Theme=Theme,
            Page="About",
            Badges=badges,
            Notifications=[[html.unescape(str(y)) for y in x] for x in Notifications],
            noNotifiers=NoNotifiers,
        )


@app.route("/shop")
def Shop():
    Uid = session.get("Uid")
    if Uid == None:
        Theme = T.FetchDefaultTheme()
        return render_template(
            "shop.html",
            UserProfileSrc="Test",
            UserName="Test",
            UserProfile="Test",
            SiteData=Text.shopTextPage,
            StaticData=Text.staticPageData,
            isloggedin=False,
            isadmin=False,
            Theme=Theme,
            Page="Shop",
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

        Notifications = N.friend.FetchNotifiers(Uid)
        NoNotifiers = False
        if Notifications == []:
            NoNotifiers = True

        Notifications = calculate_notifier_times(Notifications)

        return render_template(
            "shop.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            SiteData=Text.shopTextPage,
            StaticData=Text.staticPageData,
            SiteWelcome=random.choice(Text.homeTextPage["SiteWelcome"]) % (data[1],),
            isloggedin=True,
            isadmin=False,
            Theme=Theme,
            Page="Shop",
            Badges=badges,
            Notifications=[[html.unescape(str(y)) for y in x] for x in Notifications],
            noNotifiers=NoNotifiers,
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
    Uid = session.get("Uid")
    if Uid == None:
        Theme = T.FetchDefaultTheme()
        return render_template(
            "login.html",
            UserProfileSrc="Test",
            UserName="Test",
            UserProfile="Test",
            SiteData=Text.signinTextPage,
            StaticData=Text.staticPageData,
            isloggedin=False,
            isadmin=False,
            Theme=Theme,
            Page="Login",
        )
    else:
        return redirect(url_for("HomePage"))


@app.route("/confirmsignup", methods=["POST"])
def ConfirmSignup():
    if not Data.ValidateUser(
        request.form["user"], hashlib.sha512(request.form["pwd"].encode()).hexdigest()
    ):
        try:
            if (
                (request.form["bday"].split("-"))[0] != "00"
                and (request.form["bday"].split("-"))[1] != "00"
                and (request.form["bday"].split("-"))[2] != "0000"
                and not int((request.form["bday"].split("-"))[0]) > 33
                and not int((request.form["bday"].split("-"))[1]) > 13
                and not int((request.form["bday"].split("-"))[2])
                < int(date.today().year) - 123
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
            else:
                flash("No way thats your bithday")
                return redirect(url_for("SignUp"))
        except Exception as e:
            print(e)
            flash("An Error Occurred")
            return redirect(url_for("SignUp"))

    flash("User already exists")
    return redirect(url_for("SignUp"))


@app.route("/signup")
def SignUp():
    Uid = session.get("Uid")
    if Uid == None:
        Theme = T.FetchDefaultTheme()
        return render_template(
            "signup.html",
            UserProfileSrc="Test",
            UserName="Test",
            UserProfile="Test",
            SiteData=Text.signupTextPage,
            StaticData=Text.staticPageData,
            isloggedin=False,
            isadmin=False,
            Theme=Theme,
            Page="SignUp",
        )
    else:
        return redirect(url_for("HomePage"))


@app.route("/help")
def Help():
    Uid = session.get("Uid")
    if Uid == None:
        Theme = T.FetchDefaultTheme()
        return render_template(
            "help.html",
            UserProfileSrc="Test",
            UserName="Test",
            UserProfile="Test",
            SiteData=Text.helpTextPage,
            StaticData=Text.staticPageData,
            isloggedin=False,
            isadmin=False,
            Theme=Theme,
            Page="Help",
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

        Notifications = N.friend.FetchNotifiers(Uid)
        NoNotifiers = False
        if Notifications == []:
            NoNotifiers = True

        Notifications = calculate_notifier_times(Notifications)

        return render_template(
            "help.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            SiteData=Text.helpTextPage,
            StaticData=Text.staticPageData,
            SiteWelcome=random.choice(Text.homeTextPage["SiteWelcome"]) % (data[1],),
            isloggedin=True,
            isadmin=False,
            Theme=Theme,
            Page="Help",
            Badges=badges,
            Notifications=[[html.unescape(str(y)) for y in x] for x in Notifications],
            noNotifiers=NoNotifiers,
        )


@app.route("/ask")
def AskTheCreator():
    Uid = session.get("Uid")
    if Uid == None:
        Theme = T.FetchDefaultTheme()
        return render_template(
            "ask.html",
            UserProfileSrc="Test",
            UserName="Test",
            UserProfile="Test",
            SiteData=Text.askTextPage,
            StaticData=Text.staticPageData,
            isloggedin=False,
            isadmin=False,
            Theme=Theme,
            Page="Ask",
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

        Notifications = N.friend.FetchNotifiers(Uid)
        NoNotifiers = False
        if Notifications == []:
            NoNotifiers = True

        Notifications = calculate_notifier_times(Notifications)

        return render_template(
            "ask.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            SiteData=Text.askTextPage,
            StaticData=Text.staticPageData,
            SiteWelcome=random.choice(Text.homeTextPage["SiteWelcome"]) % (data[1],),
            isloggedin=True,
            isadmin=False,
            Theme=Theme,
            Page="Ask",
            Badges=badges,
            Notifications=[[html.unescape(str(y)) for y in x] for x in Notifications],
            noNotifiers=NoNotifiers,
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
            Theme=Theme,
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
                isguest=False,
                isadmin=admin,
                Fullname=edata[4],
                Email=edata[3],
                Phone=edata[2],
                Address=edata[1],
                Theme=Theme,
            )
        else:
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

            SentFriendRequest = N.friend.VerifyRequest(session["Uid"], uid)

            return render_template(
                "profile/profile.html",
                Uid=data[0],
                UserProfileSrc=f"/static/favicons/{data[2]}",
                UserName=data[1],
                UserProfile=f"{data[0]}",
                Description=data[3],
                isloggedin=True,
                isguest=True,
                requestsent=SentFriendRequest,
                isadmin=admin,
                Fullname=edata[4],
                Email=edata[3],
                Phone=edata[2],
                Address=edata[1],
                Theme=Theme,
            )
    except Exception as e:
        pass

    return redirect(url_for("HomePage"))


@app.route("/profile/<uid>/inventory")
def ProfileInventory(uid):
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
                "profile/inventory.html",
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
                Theme=Theme,
            )
    except Exception as e:
        pass

    return redirect(url_for("ProfileURL", uid=data[0]))


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
                Theme=Theme,
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

        badgeTime = [datetime.fromtimestamp(round(x[6])) for x in badges]

        return render_template(
            "profile/badge.html",
            Uid=data[0],
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            isloggedin=True,
            isadmin=admin,
            Badges=badges,
            LenBadges=len(badges),
            BadgeTime=badgeTime,
            BadgeRanks=S.RARITY_RANKS,
            Theme=Theme,
        )
    else:
        return redirect(url_for("HomePage"))


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
            Theme=Theme,
        )
    else:
        return redirect(url_for("HomePage"))


@app.route("/subscribe", methods=["POST"])
def Subscribe():
    if Data.ValidateID(session["Uid"]):
        E.Add(
            session["Uid"],
            request.form["email"]
        )
    else:
        return redirect(url_for("HomePage"))


@app.route("/unsubscribe", methods=["POST"])
def UnSubscribe():
    if Data.ValidateID(session["Uid"]):
        E.Remove(
            session["Uid"]
        )
    else:
        return redirect(url_for("HomePage"))


@app.route("/addfriend/<uid>")
def AddFriend(uid):
    N.friend.SendRequest(session["Uid"], uid)
    return redirect(url_for("ProfileURL", uid=uid))


@app.route("/delete/notification/<nid>")
def DeleteNotifier(nid):
    if N.delete.VerifyNotification(session["Uid"], nid):
        N.delete.Delete(session["Uid"], nid)
        return redirect(url_for("HomePage"))
    else:
        return redirect(url_for("HomePage"))


@app.route("/accept/friendrqt/<fid>")
def AcceptFriendRQT(fid):
    if N.friend.VerifyRequest(fid, session["Uid"]):
        F.newFriend.CreateFriend(session["Uid"], fid)
        return redirect(url_for("HomePage"))
    else:
        return redirect(url_for("HomePage"))


@app.route("/cancel/friendrqt/<fid>")
def DeleteFriendRQT(fid):
    if N.friend.VerifyRequest(session["Uid"], fid):
        N.friend.CancelRequest(session["Uid"], fid)
        return redirect(url_for("ProfileURL", uid=fid))
    else:
        return redirect(url_for("ProfileURL", uid=fid))


@app.route("/logout")
def LogOut():
    session.clear()
    return redirect(url_for("HomePage"))


@app.errorhandler(404)
def invalid_route(e):
    Theme = T.FetchDefaultTheme()
    return render_template(
        "404.html",
        UserProfileSrc="Test",
        UserName="Test",
        UserProfile="Test",
        SiteData=Text.errorTextPage,
        StaticData=Text.staticPageData,
        isloggedin=False,
        isadmin=False,
        Theme=Theme,
        Page="404",
    )


@app.route("/test")
def Test():
    N.friend.SendRequest(session["Uid"], session["Uid"])
    return redirect(url_for("HomePage"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, debug=True, ssl_context=("cert.pem", "key.pem"))