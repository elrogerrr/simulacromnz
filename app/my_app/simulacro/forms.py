from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import InputRequired, DataRequired

class Evento(FlaskForm):
    p_actual=IntegerField ('Personal "Evacuado"', validators=[DataRequired()])
    p_rezago=IntegerField ('Personal en "Rezago"')