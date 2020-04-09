from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Oh! a headline"
    return render_template("index1.html",headline = headline)
@app.route("/bye")
def bro():
    return "Good Bye!"
