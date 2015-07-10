from flask import Flask, request, session, redirect, url_for, render_template, flash


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return "TODO"


@app.route("/login")
def login():
    return "TODO"


@app.route("/add_post")
def add_post():
    return "TODO"


@app.route("/like_post/<post_id>")
def like_post(post_id):
    return "TODO"


@app.route("/profile/<username>")
def profile(username):
    return "TODO"


@app.route("/logout")
def logout():
    return "TODO"