from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def About():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(port=80, debug=True)
