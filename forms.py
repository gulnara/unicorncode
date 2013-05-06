from wtforms import Form, BooleanField, TextField, TextAreaField, validators

class TutorialForm(Form):
	title = TextField('Title', validators=[validators.Required()])
	tutorial = TextAreaField('Tutorial', validators=[validators.Required()])

