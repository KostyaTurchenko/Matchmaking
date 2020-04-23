from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, MultipleFileField, IntegerField
from wtforms.fields.html5 import DateTimeField, TimeField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    firstname = StringField('Имя',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Фамилия',
                            validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Почта',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Повторите пароль',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Создать')