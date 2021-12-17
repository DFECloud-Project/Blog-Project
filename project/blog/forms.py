from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms import  validators

 
class ContactMeForm(FlaskForm):
	name = StringField("Name", [validators.DataRequired('Please enter your name !')])
	email = StringField("Email", [validators.DataRequired('Please enter you email address !'), validators.Email()])
	subject = StringField("Subject", [validators.DataRequired('Please enter a Subject !')])
	message = TextAreaField("Message", [validators.DataRequired('Enter a message !')])
	submit = SubmitField("Submit")

class UpdateForm(FlaskForm):
	title = StringField("Title", [validators.DataRequired()])
	subtitle = StringField("Subtitle", [validators.DataRequired()])
	author = StringField("Author", [validators.DataRequired()])
	content = TextAreaField("Content", [validators.DataRequired()])
	submit = SubmitField("Submit")