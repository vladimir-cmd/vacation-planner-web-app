import os

from bson.objectid import ObjectId
from flask import (
    Flask, flash, render_template,
    request, session, redirect, url_for)
from flask_pymongo import PyMongo
from pip._vendor.msgpack.fallback import xrange
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env
from datetime import datetime,timedelta

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/manage_entries")
def manage_entries():
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
        # Check if password match
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if password == confirm_password:
            register_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
                "vacation_days": 25,
                "department": ""
            }

            mongo.db.users.insert_one(register_user)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration successful!")
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("Password must match. Try again")
            return redirect(url_for("register"))
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
        {"username": session["user"]})

    if session['user']:
        return render_template("profile.html", username=username)

    return redirect(url_for('login.html'))


@app.route("/profile_update/<username>", methods=["GET", "POST"])
def profile_update(username):
    # Update profile info
    if request.method == "POST":
        username = mongo.db.users.find_one(
            {"username": session["user"]})
        mongo.db.users.update_one({
            "username": username['username']
        }, {
            "$set": {
                "first_name": request.form.get("first_name"),
                "last_name": request.form.get("last_name"),
                "email_address": request.form.get("email_address"),
                "department": request.form.get("department")
            }})
        flash("Entry successfully Updated!")
        username = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("profile.html", username=username)
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_profile.html", username=username, categories=categories)


@app.route("/delete_profile/<username>", methods=["GET", "POST"])
def delete_profile(username):
    # Delete profile
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    mongo.db.entries.remove({"created_by": username['username']})
    mongo.db.users.remove({"username": username['username']})
    flash("User Successfully Deleted!")
    session.pop("user")
    return redirect(url_for('register'))


@app.route("/logout")
def logout():
    # log user out
    flash("You have been successfully logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_entry", methods=["GET", "POST"])
def add_entry():
    if request.method == "POST":
        user = mongo.db.users.find_one({'username': session["user"]})
        start_date = datetime.strptime(request.form.get("start_date"), '%d %b, %Y')
        end_date = datetime.strptime(request.form.get("end_date"), '%d %b, %Y')
        if end_date < start_date:
            flash("End Date is before start date. Please correct date entry")
            return redirect(url_for("add_entry"))

        add_entry_department = request.form.get("category_name")
        user_department = user["department"]
        if user["department"] == "":
            mongo.db.users.update_one({
                "username": user['username']
            }, {
                "$set": {
                    "department": request.form["category_name"]
                }})
        else:
            if add_entry_department != user_department:
                print("Add entry department: {} is not the same as user department: {}".format(
                    add_entry_department, user_department))
                flash("""Departments doesn't match. 
                    If you want to select different department, update your department in Profile""")
                return redirect(url_for("add_entry"))

        # Deduct from Vacation days if Regular Vacation
        entry_type = request.form.get("entry_type")
        if entry_type == "Regular Vacation":
            day_generator = (start_date + timedelta(x + 1) for x in xrange((end_date - start_date).days))
            how_many_days = sum(1 for day in day_generator if day.weekday() < 5) + 1
            update_user_days = user['vacation_days'] - how_many_days

            if update_user_days <= 0:
                flash("Current status of days left {}! You don't have enough days!".format(user['vacation_days']))
                return redirect(url_for("manage_entries"))
            else:
                mongo.db.users.update_one({
                    "username": user['username']
                }, {
                    "$set": {
                        "vacation_days": update_user_days
                    }})

        entry = {
            "category_name": request.form.get("category_name"),
            "entry_type": request.form.get("entry_type"),
            "entry_description": request.form.get("entry_description"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "created_by": session["user"]
        }
        mongo.db.entries.insert_one(entry)
        flash("Entry successfully added")

    categories = mongo.db.categories.find().sort("category_name", 1)
    vacation_types = mongo.db.vacation_types.find().sort("entry_type", 1)
    return render_template("add_entry.html", categories=categories, vacation_types=vacation_types)


@app.route("/edit_entry/<entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({'username': session["user"]})
        entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})

        username = user["username"]
        entry_username = entry["created_by"]
        if username != entry_username:
            flash("""This is not your entry. You can edit only your own!
                        Please select only your entry!""")
            return redirect(url_for("calendar_home"))

        print("User: {} and Created By: {}".format(username, entry_username))

        add_entry_department = request.form.get("category_name")
        user_department = user["department"]
        if user["department"] == "":
            mongo.db.users.update_one({
                "username": user['username']
            }, {
                "$set": {
                    "department": request.form["category_name"]
                }})
        else:
            if add_entry_department != user_department:
                print("Add entry department: {} is not the same as user department: {}".format(
                    add_entry_department, user_department))
                flash("""Departments doesn't match. 
                        If you want to select different department, update your department in Profile""")
                return redirect(url_for("manage_entries"))

        # Deduct from Vacation days if Regular Vacation
        if entry['entry_type'] == "Regular Vacation":
            start_date_from_entry = datetime.strptime(entry["start_date"], '%d %b, %Y')
            end_date_from_entry = datetime.strptime(entry["end_date"], '%d %b, %Y')

            day_generator = (start_date_from_entry + timedelta(x + 1) for x in xrange(
                (end_date_from_entry - start_date_from_entry).days))
            how_many_days_to_add = sum(1 for day in day_generator if day.weekday() < 5) + 1

            update_user_days_before_new_deduction = user['vacation_days'] + how_many_days_to_add
            mongo.db.users.update_one({
                "username": user['username']}, {
                "$set": {
                    "vacation_days": update_user_days_before_new_deduction
                }})

            user = mongo.db.users.find_one({'username': session["user"]})

            # Next we deduct new amount of vacation days
            start_date = datetime.strptime(request.form.get("start_date"), '%d %b, %Y')
            end_date = datetime.strptime(request.form.get("end_date"), '%d %b, %Y')

            day_generator = (start_date + timedelta(x + 1) for x in xrange((end_date - start_date).days))
            how_many_days = sum(1 for day in day_generator if day.weekday() < 5) + 1

            update_user_days = user['vacation_days'] - how_many_days
            mongo.db.users.update_one({
                "username": user['username']}, {
                "$set": {
                    "vacation_days": update_user_days
                }})

        # Check if End Date is Before Start Date
        start_date = datetime.strptime(request.form.get("start_date"), '%d %b, %Y')
        end_date = datetime.strptime(request.form.get("end_date"), '%d %b, %Y')
        if end_date < start_date:
            flash("End Date is before start date. Please correct date entry")
            return redirect(url_for("manage_entries"))

        update = {
            "category_name": request.form.get("category_name"),
            "entry_type": request.form.get("entry_type"),
            "entry_description": request.form.get("entry_description"),
            "start_date": request.form.get("start_date"),
            "end_date": request.form.get("end_date"),
            "created_by": session["user"]
        }

        mongo.db.entries.update({"_id": ObjectId(entry_id)}, update)
        flash("Entry successfully Updated!")

    entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    vacation_types = mongo.db.vacation_types.find().sort("entry_type", 1)
    return render_template("edit_entry.html", categories=categories, vacation_types=vacation_types, entry=entry)


@app.route("/delete_entry/<entry_id>")
def delete_entry(entry_id):
    user = mongo.db.users.find_one({'username': session["user"]})
    entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
    # Deduct from Vacation days if Regular Vacation
    if entry['entry_type'] == "Regular Vacation":
        start_date_from_entry = datetime.strptime(entry["start_date"], '%d %b, %Y')
        end_date_from_entry = datetime.strptime(entry["end_date"], '%d %b, %Y')

        day_generator = (start_date_from_entry + timedelta(x + 1) for x in xrange(
            (end_date_from_entry - start_date_from_entry).days))
        how_many_days_to_add = sum(1 for day in day_generator if day.weekday() < 5) + 1

        update_user_days_before_new_deduction = user['vacation_days'] + how_many_days_to_add
        mongo.db.users.update_one({
            "username": user['username']}, {
            "$set": {
                "vacation_days": update_user_days_before_new_deduction
            }})

    # Next Lets delete the user entry
    mongo.db.entries.remove({"_id": ObjectId(entry_id)})
    flash("Task Successfully Deleted!")
    return redirect(url_for("manage_entries"))


@app.route("/calendar_home")
def calendar_home():
    entries = mongo.db.entries.find()
    return render_template("calendar_home.html", entries=entries)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
