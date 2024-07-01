from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email

class detailsForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired("Enter your Name")])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField("Address")
    email = StringField("Email", validators=[DataRequired("Enter your Email address"), Email("Enter a correct Email address")])
    age = IntegerField("Age")
    programming_language = SelectField("Programming Language", choices=[("C#", "C++"), ("PY", "python")])
    submit = SubmitField("Submit")
                        
                        
                    