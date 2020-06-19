from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
class UpdateProfile(FlaskForm):
	bio = TextAreaField('Tell us something about you',validators= [Required()])
	submi = SubmitField('Submit')
