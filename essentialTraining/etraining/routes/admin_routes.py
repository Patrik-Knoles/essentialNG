from flask import Flask, render_template, make_response, request, redirect, flash, session
from sqlalchemy import values
from etraining import  app, db, csrf
from etraining.forms import *
from etraining.models import *
from werkzeug.security import generate_password_hash, check_password_hash
