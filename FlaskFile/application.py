from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, world!!!!!"
@app.route("/moksha")
def moksha():
    return "Hello, Moksha!!!"
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize();
    return f"<h1>Hello, {name}</h1>"
@app.route("/bsdk")
def fuckboi():

