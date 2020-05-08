from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, MultipleFileField, IntegerField
from wtforms.fields.html5 import DateTimeField, TimeField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Ник', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Ник',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    #confirm_password = PasswordField('Повторите пароль',
    #                                 validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Создать аккаунт')
