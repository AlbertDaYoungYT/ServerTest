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
        img = Image.open(UPLOAD_FOLDER + "/" + filename) # Open image
        img = img.resize((512, 512), Image.ANTIALIAS) # Resize image
        img.save(UPLOAD_FOLDER + "/" + filename, format='JPEG') # Save resized image
        # print('upload_image filename: ' + filename)
        flash("Image successfully uploaded and displayed below")
        return render_template("upload.html")
    else:
        flash("Allowed image types are -> png, jpg, jpeg, gif")
        return redirect(request.url)


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


@app.route("/about")
def About():
    return render_template(
        "about.html",
        content=Text.aboutTextPage,
        UserProfileSrc="Test",
        UserName="Test",
        UserProfile="Test",
        isloggedin=True,
        isadmin=False,
    )


@app.route("/shop")
def Shop():
    return render_template(
        "shop.html",
        content=Text.ShopItems,
        UserProfileSrc="Test",
        UserName="Test",
        UserProfile="Test",
        isloggedin=True,
        isadmin=False,
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
    return render_template("login.html")


@app.route("/logout")
def LogOut():
    session.clear()
    return redirect(url_for("HomePage"))


@app.route("/confirmsignup", methods=["POST"])
def ConfirmSignup():
    if not Data.ValidateUser(
        request.form["user"], hashlib.sha512(request.form["pwd"].encode()).hexdigest()
    ):
        try:
            if (
                len(request.form["bday"]) == 10
                and len(request.form["bday"].split("-")) == 3
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
        except Exception:
            flash("Some fields are not filled out correctly")
            return redirect(url_for("SignUp"))

    flash("User already exists")
    return redirect(url_for("SignUp"))


@app.route("/signup")
def SignUp():
    return render_template("signup.html")


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


if __name__ == "__main__":
    app.run(host="192.168.1.30", port=80, debug=True)
