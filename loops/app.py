from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    names = ["Leah","Mia","Gabbie"]
    return render_template("index.html",names=names)
