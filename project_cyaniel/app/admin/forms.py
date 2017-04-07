from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CharacterForm(FlaskForm):
    """
    Form for admin to add or edit a character
    """
    character_name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')