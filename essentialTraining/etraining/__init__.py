from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from etraining import config

app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile("config.py")
app.config.from_object(config.LiveConfig)
csrf = CSRFProtect(app)

db = SQLAlchemy(app)

from etraining import routes, models
from etraining.routes import user_routes, admin_routes

#import any other variable, object, module you would need in this app 

"""Things required here:
1.) instantiate an object of flask

2.) import your route

3.) load your config file if you wish to or load it on your server file(myapp.py)
"""