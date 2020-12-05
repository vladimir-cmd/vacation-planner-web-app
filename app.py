import os
from flask import (
    Flask, flash, render_template, 
    request, session, redirect, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_entries")
def get_entries():
    entries = list(mongo.db.entries.find())
    return render_template("manage_entries.html", entries=entries)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if user exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"],
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}. Enjoy!".format(
                    request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password entered
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get username from Mongo DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session['user']:
        return render_template("profile.html", username=username)

    return redirect(url_for('login.html'))


@app.route("/logout")
def logout():
    # log user out
    flash("You have been successfully logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_entry", methods=["GET", "POST"])
def add_entry():
    if request.method == "POST":
        half_day = "on" if request.form.get("half_day") else "off"
        entry = {
            "category_name": request.form.get("category_name"),
            "entry_type": request.form.get("entry_type"),
            "entry_description": request.form.get("entry_description"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "half_day": half_day,
            "created_by": session["user"]
        }
        mongo.db.entries.insert_one(entry)
        flash("Entry successfully added")
        return redirect(url_for("get_entries"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    vacation_types = mongo.db.vacation_types.find().sort("entry_type", 1)
    return render_template("add_entry.html", categories=categories, vacation_types=vacation_types)


@app.route("/edit_entry/<entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    if request.method == "POST":
        half_day = "on" if request.form.get("half_day") else "off"
        update = {
            "category_name": request.form.get("category_name"),
            "entry_type": request.form.get("entry_type"),
            "entry_description": request.form.get("entry_description"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "half_day": half_day,
            "created_by": session["user"]
        }
        mongo.db.entries.update({"_id": ObjectId(entry_id)}, update)
        flash("Entry successfully Updated!")

    entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    vacation_types = mongo.db.vacation_types.find().sort("entry_type", 1)
    return render_template("edit_entry.html", categories=categories, vacation_types=vacation_types, entry=entry)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
