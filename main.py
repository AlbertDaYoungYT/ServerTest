from flask import Flask, render_template
from flask_cors import CORS

import data.text as Text

app = Flask(__name__)
CORS(app)

@app.route("/")
def HomePage():
    return render_template('index.html', UserProfileSrc="Test", UserName="Test", isloggedin=True, isadmin=False)

@app.route("/about")
def About():
    return render_template("about.html", content=Text.aboutTextPage, UserProfileSrc="Test", UserName="Test", isloggedin=True, isadmin=False)

@app.route("/shop")
def Shop():
    return render_template("shop.html", content=Text.ShopItems, UserProfileSrc="Test", UserName="Test", isloggedin=True, isadmin=False)

@app.route("/signin")
def SignIn():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)