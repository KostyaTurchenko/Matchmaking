from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean)
    rooms = db.relationship('Room', secondary='user_room', backref='participants', lazy=True)
    user_rooms = db.relationship('Room', backref='host', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    start_time = db.Column(db.DateTime)
    max_num_of_player = db.Column(db.Integer)
    host_message = db.Column(db.String(2020))
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))

    def __repr__(self):
        return f"Room('{self.name}')"


class UserRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    game_genre_id = db.Column(db.Integer, db.ForeignKey('game_genre.id'))
    rooms = db.relationship('Room', backref='game', lazy=True)

    def __repr__(self):
        return str(self.name)


class GameGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    games = db.relationship('Game', backref='genre', lazy=True)

    def __repr__(self):
        return str(self.name)


