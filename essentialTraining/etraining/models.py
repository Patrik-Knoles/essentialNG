from  datetime import datetime
from etraining import db 


class Admin(db.Model): 
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False) 
    guest_pwd = db.Column(db.String(100), nullable=False)    
	
class Additional_skills(db.Model): 
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    skill =db.Column(db.String(255), nullable=False) 
    level =db.Column(db.String(100), nullable=False)

class Education(db.Model):
    #columname=db.Column(db.datatype())
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    school_name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=True)
    end_date = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=True)
    resume = db.Column(db.String(255), nullable=False)

class Jobs(db.Model):
    #columname=db.Column(db.datatype())
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=True)
    end_date = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=True)

class Primary_skill(db.Model): 
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    skill =db.Column(db.String(255), nullable=False) 

class States(db.Model): 
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name =db.Column(db.String(255), nullable=False)

class User(db.Model): 
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)
    residential_address = db.Column(db.String(100), nullable=False)
    state_id = db.Column(db.Integer(), db.ForeignKey("states.id"))
    password = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    skill_id = db.Column(db.Integer(), db.ForeignKey("primary_skill.id"))
    primary_experience = db.Column(db.String(255), nullable=False)
    english_proficiency = db.Column(db.String(255), nullable=False)
    referred_by = db.Column(db.String(255), nullable=True)
    resume = db.Column(db.String(255), nullable=False)
    profile_photo = db.Column(db.String(255), nullable=True)
    cover_photo = db.Column(db.String(255), nullable=True)
    # education_id = db.Column(db.Integer(), db.ForeignKey("education.id"))
    # jobs_id = db.Column(db.Integer(), db.ForeignKey("jobs.id"))
    # skill2_id = db.Column(db.Integer(), db.ForeignKey("additional_skills.id"))
    date_registered = db.Column(db.DateTime(), default=datetime.utcnow())

    # relationship
    state = db.relationship("States", backref="user_state")
    skill = db.relationship("Primary_skill", backref="user_skill")
    # education = db.relationship("Education", backref="user_education")
    # jobs = db.relationship("Jobs", backref="user_jobs")
    # skill2 = db.relationship("Additional_skills", backref="user_skill2")
    

# class Guest_gift(db.Model):
#     g_giftid = db.Column(db.Integer(), db.ForeignKey('gifts.gift_id'))
#     g_guestid =db.Column(db.Integer(), db.ForeignKey('guests.guest_id')) 
    