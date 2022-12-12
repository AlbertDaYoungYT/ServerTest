from flask import *
from werkzeug.utils import *
from flask_cors import CORS
from PIL import Image, ImageOps
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


ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


import about
import applyadmin
import home
import profile
import shop
import signin
import signup


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        flash("No image selected for uploading")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        img = Image.open(UPLOAD_FOLDER + "/" + filename)  # Open image
        img = img.resize((512, 512), Image.ANTIALIAS)  # Resize image
        img.save(UPLOAD_FOLDER + "/" + filename, format="JPEG")  # Save resized image
        # print('upload_image filename: ' + filename)
        flash("Image successfully uploaded and displayed below")
        return render_template("upload.html")
    else:
        flash("Allowed image types are -> png, jpg, jpeg, gif")
        return redirect(request.url)

@app.route("/logout")
def LogOut():
    session.clear()
    return redirect(url_for("HomePage"))


if __name__ == "__main__":
    app.run(host="192.168.115.138", port=80, debug=True)
