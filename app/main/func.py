from app.models import *


class Navigation:
    def __init__(self, db):
        self.db = db

    def get_rooms_by_genre(self, genre_id):
        games_id = [game.id for game in Game.query.filter_by(game_genre_id=genre_id).all()]
        rooms = Room.query.filter(Room.id.in_(games_id)).all()
        return rooms

    def get_rooms_by_game(self, game_id):
        return Room.query.filter_by(game_id=game_id).all()
