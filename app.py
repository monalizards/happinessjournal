import re # https://docs.python.org/3/howto/regex.html
from passlib.hash import sha256_crypt
from datetime import datetime
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

# Render error message
def error(message, code=400):
    return render_template("error.html", message=message, code=code)

# Hashing password
def hash(password):
    return sha256_crypt.encrypt(password)

# Verify password
def verify(password, hash):
    return sha256_crypt.verify(password, hash)

# Convert date to sql datetime
def convert_date(date):
    return datetime.fromisoformat(date).isoformat()

@app.route("/")
def index():
    id = session.get("user_id")
    if id != None:
        records = db.execute("SELECT * FROM records WHERE id = :id", id=id)
    else:
        records = None
    return render_template("index.html", records=records)

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    # Perform checks and insert when a form is submitted via POST
    if request.method == "POST":
        # Ensure all fields were filled
        if not request.form.get("username") or not request.form.get("email") or not request.form.get("password") or not request.form.get("confirm") or not request.form.get("birthday"):
            return error("Missing field(s)")
        # Ensure username doesn't already exist
        elif db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username")):
            return error("username already exists")
        # Ensure password and confirmation matched
        elif request.form.get("password") != request.form.get("confirm"):
            return error("password and confirmation must match")
            
        # Insert new user into users
        id = db.execute("INSERT INTO users (username, email, hash, birthday) values (?,?,?,?)",
                   request.form.get("username"),
                   request.form.get("email"),
                   hash(request.form.get("password")),
                   convert_date(request.form.get('birthday')))
        
        # Remember which user has logged in
        session["user_id"] = id
        # Redirect user to home page
        return redirect("/")
        
    
    # Render registration form when a form is 
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    # Perform checks and insert when a form is submitted via POST
    if request.method == "POST":
        # Ensure all fields were filled
        if not request.form.get("username") or not request.form.get("password"):
            return error("Missing field(s)")
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        # Ensure username exists and password is correct
        if len(rows) != 1 or not verify(request.form.get("password"), rows[0]["hash"]):
            return error("invalid username and/or password")
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")
    # Render login form when a form is 
    else:
        return render_template("login.html")

# Logout: clear session
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
