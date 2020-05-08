from app.models import User, Room
from app import bcrypt
from flask_login import login_user


class Accession:
    def __init__(self, db):
        self.db = db

    def login(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return True
        return False

    def registration(self, username, email, password):
        if not User.query.filter_by(username=username).first() and not User.query.filter_by(email=email).first():
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, email=email, password=hashed_password)

            self.db.session.add(user)
            self.db.session.commit()
            return True
        return False

    def join_room(self, user, room):
        pass

    def leave_room(self, user, room):
        pass

    def get_user_information(self, user):
        pass

