from app.models import *


class Navigation:
    def __init__(self, db):
        self.db = db

    def get_games_and_rooms_by_genre(self, genre_id):
        games = Game.query.filter_by(game_genre_id=genre_id).all()
        games_id = [game.id for game in games]
        rooms = Room.query.filter(Room.id.in_(games_id)).all()
        return games, rooms

    def get_rooms_by_game(self, game_id):
        return Room.query.filter_by(game_id=game_id).all()

