from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class NewPlane(FlaskForm):
    reg = StringField('Lajstrom', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Felszállít')