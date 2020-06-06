from flask import render_template, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app.main.func import Navigation
from app.models import Genre, Room
from app import db

main = Blueprint('main', __name__)
navig = Navigation(db)
genres = Genre.query.all()
games = []          # СОМНИТЕЛЬНОЕ РЕШЕНИЕ С ГЛОБАЛЬНЫМИ ПЕРЕМЕННЫМИ!!!
rooms = []


@main.route("/home")
@login_required
def home():
    try:
        s = request.args.get('s')
        if s:
            global rooms
            rooms = Room.query.filter(Room.name.contains(s)).all()
        return render_template("main page.html", rooms=rooms, games=games, genres=genres)
    except Exception as e:
        print(e)


@main.route("/about")
@login_required
def about():
    render_template("about.html")


@main.route("/roomsbygenre/<int:genre_id>")
@login_required
def get_rooms_by_genre(genre_id):
    try:
        global games, rooms
        games, rooms = navig.get_games_and_rooms_by_genre(genre_id)
        return render_template("main page.html", rooms=rooms, games=games, genres=genres)
    except Exception as e:
        print(e)


@main.route("/roomsbygame/<int:game_id>")
@login_required
def get_rooms_by_game(game_id):
    try:
        global rooms
        rooms = navig.get_rooms_by_game(game_id)
        return render_template("main page.html", rooms=rooms, games=games, genres=genres)
    except Exception as e:
        print(e)