import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB


@app.route("/profile/<uid>")
def ProfileURL(uid):
    try:
        if uid == str(session["Uid"]):
            data = list(UP.FetchUserdata(uid))
            edata = list(UP.FetchEUserdata(uid))
            try:
                if "".join(data) == "NOTFOUND":
                    return redirect(url_for("LogOut"))
            except Exception:
                pass

            try:
                Theme = session["theme"]
            except Exception:
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
    except Exception:
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
            except Exception:
                pass

            try:
                Theme = session["theme"]
            except Exception:
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
    except Exception:
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