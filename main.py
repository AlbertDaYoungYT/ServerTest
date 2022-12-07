from flask import Flask, render_template
from flask_cors import CORS

import data.text as Text

app = Flask(__name__)
CORS(app)

@app.route("/")
def HomePage():
    return render_template('index.html')

@app.route("/about")
def About():
    return render_template("about.html", content=Text.aboutTextPage)

@app.route("/shop")
def Shop():
    return render_template("shop.html", content=Text.ShopItems, UserProfileSrc="Test", UserName="Test", isloggedin=True)

@app.route("/signin")
def SignIn():
    return render_template("admin/index.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)