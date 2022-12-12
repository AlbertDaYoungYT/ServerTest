from flask import *
from werkzeug.utils import *
from flask_cors import CORS
import hashlib
import uuid
import os

import data.text as Text
import modules.DataBase as Data
import modules.UserProfile as UP
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


import about
import admin
import applyadmin
import home
import profile
import shop
import signin
import signup


@app.route("/logout")
def LogOut():
    session.clear()
    return redirect(url_for("HomePage"))


if __name__ == "__main__":
    app.run(host="192.168.111.240", debug=True)
