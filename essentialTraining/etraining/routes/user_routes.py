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
    return render_template("user/signup.html")

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