from __main__ import app
import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB


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
            "index.html",
            UserProfileSrc=f"/static/favicons/{data[2]}",
            UserName=data[1],
            UserProfile=f"{data[0]}",
            isloggedin=True,
            isadmin=admin,
            color1=Theme[1],
            color2=Theme[2],
            color3=Theme[3],
            color4=Theme[4],
            color5=Theme[5],
        )