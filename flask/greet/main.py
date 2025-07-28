from flask import Flask
from flask import Response
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return Response("Hello, world!", mimetype="text/plain")

@app.route("/hi")
def hi():
    return Response("hi", mimetype="text/plain")

@app.route("/hi/<name>")
def hi_name(name):
    return Response(f"hi, {escape(name)}!", mimetype="text/plain")

@app.route("/bye")
def bye():
    return Response("bye", mimetype="text/plain")

@app.route("/bye/<name>")
def bye_name(name):
    return Response(f"bye, {escape(name)}!", mimetype="text/plain")
