from flask import *
from flask_cors import CORS
import hashlib
import uuid

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import modules.Theme as T
import data.settings as S
import db as DB

app = Flask(__name__)
CORS(app)


app.secret_key = S.SECRET
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def HomePage():
    Uid = session.get('Uid')
    if Uid == None:
        Theme = T.FetchDefaultTheme()
        return render_template('index.html', UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=False, isadmin=False, color1=Theme[1], color2=Theme[2], color3=Theme[3], color4=Theme[4], color5=Theme[5])
    else:
        data = list(UP.FetchUserdata(Uid))
        if ''.join(data) == "NOTFOUND":
            return redirect(url_for("LogOut"))

        try: Theme = session["theme"]
        except Exception: Theme = "default"
        Theme = T.FetchTheme(Theme)

        if data[-1] == "False":
            admin = False
        else:
            admin = True

        return render_template('index.html', UserProfileSrc=f"static/favicons/{data[2]}", UserName=data[1], UserProfile=f"{data[0]}", isloggedin=True, isadmin=admin, color1=Theme[1], color2=Theme[2], color3=Theme[3], color4=Theme[4], color5=Theme[5])

@app.route("/about")
def About():
    return render_template("about.html", content=Text.aboutTextPage, UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=True, isadmin=False)

@app.route("/shop")
def Shop():
    return render_template("shop.html", content=Text.ShopItems, UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=True, isadmin=False)

@app.route("/confirmsignin", methods=["POST"])
def ConfirmLogin():
    if Data.ValidateUser(request.form["user"], hashlib.sha512(request.form["pwd"].encode()).hexdigest()):
        Uid = Data.FetchUID(request.form["user"], hashlib.sha512(request.form["pwd"].encode()).hexdigest())
        if Uid != False:
            session["Uid"] = Uid
            return redirect(url_for('HomePage'))
        else:
            flash("Uid could not be found, please contact an admin")
            return redirect(url_for("SignIn"))


    flash("Incorrect Username or Password")
    return redirect(url_for("SignIn"))
    
@app.route("/signin")
def SignIn():
    return render_template("login.html")

@app.route("/logout")
def LogOut():
    session.clear()
    return redirect(url_for('HomePage'))


@app.route("/confirmsignup", methods=["POST"])
def ConfirmSignup():
    if not Data.ValidateUser(request.form["user"], hashlib.sha512(request.form["pwd"].encode()).hexdigest()):
        Uid = uuid.uuid1()
        session["Uid"] = Uid
        session["theme"] = "default"
        Data.CreateUser(Uid, request.form["dname"], request.form["user"], hashlib.sha512(request.form["pwd"].encode()).hexdigest())
        
        return redirect(url_for('HomePage'))

    flash("User already exists")
    return redirect(url_for("SignUp"))

@app.route("/signup")
def SignUp():
    return render_template("signup.html")


@app.route("/profile/<uid>")
def ProfileURL(uid):
    try:
        if uid == str(session["Uid"]):
            return str(UP.FetchUserdata(uid))
    except Exception:
        pass

    return redirect(url_for("HomePage"))

if __name__ == '__main__':
    app.run(host="192.168.111.240", debug=True)
