from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, InputRequired


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[InputRequired(), Email()])
    password = PasswordField(label='Password', validators=[InputRequired(), Length(min=6, max=12,
                                                                                   message='Password must be at least '
                                                                                           '6 characters long')])
    submit = SubmitField('Login')
