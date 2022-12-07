from flask import *
from flask_cors import CORS
import hashlib
import uuid

import data.text as Text
import db as DB

app = Flask(__name__)
CORS(app)

@app.route("/")
def HomePage():
    request.args.get('id')
    return render_template('index.html', UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=False, isadmin=False)

@app.route("/about")
def About():
    return render_template("about.html", content=Text.aboutTextPage, UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=True, isadmin=False)

@app.route("/shop")
def Shop():
    return render_template("shop.html", content=Text.ShopItems, UserProfileSrc="Test", UserName="Test", UserProfile="Test", isloggedin=True, isadmin=False)

@app.route("/confirmsignin", methods=["POST"])
def ConfirmLogin():
    session["id"] = uuid.uuid1()
    return render_template('index.html')

@app.route("/signin")
def SignIn():
    return render_template("login.html")

@app.route("/logout")
def LogOut():
    return "None"

if __name__ == '__main__':
    app.run(debug=True)