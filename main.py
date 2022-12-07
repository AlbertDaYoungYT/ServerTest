from flask import *
from flask_cors import CORS
import hashlib
import uuid

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
import data.settings as S
import db as DB

app = Flask(__name__)
CORS(app)


app.secret_key = S.SECRET
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def HomePage():
    Uid = session.get('id')
    if Uid == None:
        return render_template('index.html', UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=False, isadmin=False)
    else:
        data = list(UP.FetchUserdata(Uid))
        print(data)
        return render_template('index.html', UserProfileSrc=f"static/favicons/{data[2]}", UserName=data[1], UserProfile=f"{data[1].lower()}", isloggedin=True, isadmin=False)

@app.route("/about")
def About():
    return render_template("about.html", content=Text.aboutTextPage, UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=True, isadmin=False)

@app.route("/shop")
def Shop():
    return render_template("shop.html", content=Text.ShopItems, UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=True, isadmin=False)

@app.route("/confirmsignin", methods=["POST"])
def ConfirmLogin():
    ID = uuid.uuid1()
    session["id"] = ID
    Data.CreateUser(ID, request.form["user"], request.form["pwd"])
    return redirect(url_for('HomePage'))

@app.route("/signin")
def SignIn():
    return render_template("login.html")

@app.route("/logout")
def LogOut():
    session.clear()
    return redirect(url_for('HomePage'))

if __name__ == '__main__':
    app.run(debug=True)