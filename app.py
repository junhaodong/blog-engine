#!/usr/bin/python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/<name>") #SEE FLASK DOCUMENTATION
def post():
    return render_template("post.html")

if __name__ == "__main__":
    app.debug=True
    app.run()