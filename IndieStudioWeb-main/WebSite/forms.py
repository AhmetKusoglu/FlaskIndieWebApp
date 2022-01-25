from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import Length,Email,DataRequired,EqualTo,ValidationError


class RegistrationForms(FlaskForm):
    username=StringField(label="Username",validators=[DataRequired(),Length(min=4,max=10)])
    email_address=StringField(label="Email",validators=[Email(),DataRequired(),Length(min=4)])
    password1=PasswordField(label="Password",validators=[DataRequired(),Length(min=4)])
    password2=PasswordField(label="Confirm Password",validators=[EqualTo("password1")])
    submit=SubmitField(label="Register")