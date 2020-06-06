from app.models import User, Room, UserRoom
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

    def join_room(self, user_id, room):
        user = User.query.get(user_id)
        if user and room and not user.rooms.count(room) and not user.user_rooms.count(room)\
                and len(room.participants) < room.max_num_of_player:
            user.rooms.append(room)
            self.db.session.commit()
            return True
        return False

    def leave_room(self, user_id, room_id):
        user = User.query.get(user_id)
        room = Room.query.get(room_id)
        if user and user.rooms.count(room):
            UserRoom.query.filter_by(user_id=user_id,
                                     room_id=room_id).delete()
            self.db.session.commit()
            return True
        return False


    def get_user_information(self, user):
        rooms = user.rooms
        user_rooms = user.user_rooms
        return rooms, user_rooms



