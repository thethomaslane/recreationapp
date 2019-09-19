from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ActivityForm(FlaskForm):
    outdoors = BooleanField('Do you like the outdoors?')
    active = BooleanField('Do you like to be active?')
    submit = SubmitField('Submit')
