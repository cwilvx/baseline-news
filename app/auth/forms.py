from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
	email = StringField('Your Email Adress',validators = [Required(),Email()])
	password = PasswordField('Password',validators=[Required()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	email = StringField('Your Email Adress',validators=[Required()])
	username = StringField('Enter your username',validators=[Required()])
	password = PasswordField('Password',validators=[Required(),EqualTo('password2',message='Passwords Must Match')])
	password2 = PasswordField('Confirm Passwords',validators=[Required()])
	submit = SubmitField('Sign Up')

def validate_email(self,data_field):
	if User.query.filter_by(email = data_field.data).first():
		raise ValidationError('Email already exists')

def validate_username(self,data_field):
	if User.query.filter_by(username = data_field.data).first():
		raise ValidationError('Username already exists, choose another')