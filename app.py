from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functools import wraps

# Configure application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure database
db = SQL("sqlite:///journal.db")

# helper functions
# Ensure user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# TODO: index
@app.route("/")
@login_required
def index():
    if session.get("user_id") is None:
        return "Not logged in"
    return "logged_in"

# TODO: login
@app.route("/login")
def login():
    return "login form"

# Logout: clear session
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# TODO: error
# @app.route("/error")
# def error():
#     return "error form"