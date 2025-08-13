from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class KycForm(FlaskForm):
    fullname = StringField("Full Name",validators=[
        DataRequired(message="fullname is mandate"),
        Regexp(r"^[A-Za-z ]{3,50}$", message="Invalid Fullname")
    ])
    passcode = PasswordField("Passcode",validators=[
        DataRequired(message="Passcode is mandate"),
        Regexp(r"^(?=.*[@#$&!])(?=.+[0-9])[A-Za-z0-9@#$&!]{8,}$",message="Invalid passcode")
    ])
    email = EmailField("Email",validators=[
        DataRequired(message="email is mandate"),
        Regexp(r"^[a-z0-9-]{3,}@[a-z]{2,}\.[a-z]{2}", message="Invalid email")
    ])
    aadhaar = StringField("Aadhaar",validators=[
        Regexp(r"^[0-9]{12}$",message="Invalid Aadhaar")
    ])
    pan = StringField("PAN Number",validators=[
        Regexp(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}",message="Invalid Pan")
    ])
    type = RadioField("Account type",choices=[
        ("savings","SA"),
        ("current","CA")
    ],validators=[
        DataRequired(message="Select any account type")
    ])
    branch = SelectField("Select Branch",choices=[
        ("manglore","Mangaluru"),
        ("banglore","Bengaluru"),
        ("moodbidri","Moodbidri"),
    ], validators=[
        DataRequired(message="Select any branch")
    ])
    declaration = BooleanField("I agree all details are true", validators=[
        DataRequired(message="need to declare")
    ])
    submit = SubmitField("Submit KYC")