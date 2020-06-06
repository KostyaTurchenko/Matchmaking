from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, MultipleFileField, IntegerField
from wtforms.fields.html5 import DateTimeLocalField, DateTimeField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Game


class RoomForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    host_message = StringField('Сообщение')
    game_options = QuerySelectField(query_factory=lambda: Game.query)
    start_time = DateField('Дата проведения', validators=[DataRequired()])
    max_num_of_player = IntegerField('Количество игроков')
    submit = SubmitField('Сохранить')