# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, DateField
from wtforms.validators import DataRequired
import datetime


class CharacterForm(FlaskForm):
    """
    Form for admin to add or edit a characters
    """
    id = HiddenField('id')
    last_update = HiddenField(default=datetime.datetime.now())
    character_name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')