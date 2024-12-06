from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class VisitInterestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    user_id = IntegerField('User ID', validators=[DataRequired(), NumberRange(min=1)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=15)])
    willing_to_come_to_zoo = BooleanField('Willing to Visit the Zoo')
    willing_to_come_to_charminar = BooleanField('Willing to Visit Charminar')
    submit = SubmitField('Submit')
