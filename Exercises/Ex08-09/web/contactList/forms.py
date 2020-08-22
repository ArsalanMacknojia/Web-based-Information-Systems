from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from contactList.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=60)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. Please try something else!')


class CreateContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=20)])
    email = StringField('Email', validators=[Email(), Length(max=120)])
    phone_number = StringField('Phone Number', validators=[Length(max=16)])
    notes = TextAreaField('Notes', validators=[Length(max=1000)])
    submit = SubmitField('Create Contact')


class UpdateContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=20)])
    email = StringField('Email', validators=[Email(), Length(max=120)])
    phone_number = StringField('Phone Number', validators=[Length(max=16)])
    notes = TextAreaField('Notes', validators=[Length(max=1000)])
    submit = SubmitField('Update Contact')
