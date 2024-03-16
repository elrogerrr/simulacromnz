from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, DataRequired

class Usuario(FlaskForm):
    name=StringField ('name', validators=[DataRequired()])