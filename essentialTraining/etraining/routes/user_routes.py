import random, os
from flask import Flask, render_template, make_response, abort, redirect, flash, session, request
from sqlalchemy import values
from etraining import  app, db, csrf
from etraining.forms import *
from etraining.models import *
from werkzeug.security import generate_password_hash, check_password_hash


# The routes for all pages requested by the user;

@app.route("/", methods=["POST","GET"])
def home():
    return render_template("user/index.html")

@app.route("/about/", methods=["POST","GET"])
def about():
    return render_template("user/about.html")

@app.route("/contact/", methods=["POST","GET"])
def contact():
    return render_template("user/contact.html")

@app.route("/discover/talent/", methods=["POST","GET"])
def talent():
    return render_template("user/jobs.html")

@app.route("/job/seeker/", methods=["POST","GET"])
def seeker():
    return render_template("user/signup.html")

@app.route("/profile/", methods=["POST","GET"])
def profile():
    return render_template("user/profile.html")


# For authentication

@app.route("/signup/", methods=["POST","GET"])
def signup():
    skills = db.session.query(Primary_skill).all()
    state = db.session.query(States).all()
    return render_template("user/signup.html",skills=skills, state=state)

@app.route("/signing/", methods=["POST","GET"])
def sigining():
    if request.method == "GET":
        return render_template("user/signup.html")
    else:
        if request.files != "":
            # Retrieve the details of the user from the first page

            firstName = request.form['firstName']
            lastName = request.form['lastName']
            phone = request.form['phone']
            email = request.form['email']
            address = request.form['address']
            state = request.form.getlist('state')
            password = request.form['password']
            re_password = request.form['re_password']
            gender = request.form.getlist('gender')
            dob = request.form['date']

            # Retrieving from the second page
            skill = request.form.getlist('skill')
            experience = request.form.getlist('experience_level')

            # Retrieving from third page
            language = request.form.getlist('language')
            referral = request.form['referral']
            resume = request.files['resume']

            # Checking if resume insterted is in pdf format
            allowed = [".pdf"]
            file_name = resume.filename

            # Converting resume to a random string
            newname = random.random() * 1000
            file, ext = os.path.splitext(file_name)

            if ext in allowed:
                file_path = "etraining/static/uploads/myresume"+str(newname)+ext
                resume.save(f"{file_path}")

                for a in state:
                    for b in skill:
                        for c in gender:
                            for d in experience:
                                for e in language:
                                    user = User()
                                    user.first_name = firstName
                                    user.last_name = lastName
                                    user.email_address = email
                                    user.phone_number = phone
                                    user.residential_address = address
                                    user.state_id = a
                                    user.password = password
                                    user.gender = c
                                    user.dob = dob
                                    user.skill_id = b
                                    user.primary_experience = d
                                    user.english_proficiency = e
                                    user.referred_by = referral
                                    user.resume = str(newname)+ext
                                    db.session.add(user)
                                    db.session.commit()
                                    return request.form
            else:
                flash("Please Select a valid file format")
                return("/signup/")
        else:
            flash("Please Select a valid file format")
            return("/signup/")





@app.route("/login/", methods=["POST","GET"])
def login():
    return render_template("user/login.html")

@app.route("/verify/email/", methods=["POST","GET"])
def verify_mail():
    if request.method == "GET":
       return render_template("user/verify.html")
    else:
        return redirect("/")

@app.route("/forgot/password/", methods=["POST","GET"])
def forgot_pwd():
    if request.method == "POST":
       return render_template("user/forgotpwd.html")
    else:
        return redirect("/")


@app.errorhandler(404)
def pagenotfound(error):
    return render_template("user/404.html",error=error),404