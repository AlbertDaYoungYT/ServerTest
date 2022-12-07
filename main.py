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
    return render_template("about.html", data=Text.aboutTextPage)

if __name__ == '__main__':
    app.run(port=80, debug=True)
