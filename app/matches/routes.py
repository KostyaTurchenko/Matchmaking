from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from app.matches.func import Editor
from app.matches.forms import *
from app.models import Room
from app import db

matches = Blueprint('main', __name__)
editor = Editor(db)


@matches.route("/editroom/<int:room_id>", methods=['GET', 'POST'])
@login_required
def edit_match(room_id=0):
    form = RoomForm()
    room = Room.query.get(room_id)
    if form.validate_on_submit():
        if room:
            room.name = form.name.data
            room.max_num_of_player = form.max_num_of_player.data
            room.start_time = form.start_time.data
            room.host_message = form.host_message.data
            room.game = form.game_options.data
            db.session.commit()
        else:
            editor.create_room(current_user, form.name.data, form.start_time.data,
                               form.max_num_of_player.data, form.game_options.data,
                               form.host_message.data)  # возвращает false если слишком много созданных комнат, добавлю уведомление если фолз, если успею

        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('show_room'))

    if room:
        form.name.data = room.name
        form.max_num_of_player.data = room.max_num_of_player
        form.start_time.data = room.start_time
        form.game_options.data = room.game
        form.host_message.data = room.host_message

    return render_template('make_match.html', form=form)


@matches.route("/delroom/<int:room_id>")
@login_required
def delete_room(room_id):
    editor.delete_room(current_user, room_id)
    return redirect(url_for('user_page'))


@matches.route("/userpage")
@login_required
def user_page():
    return render_template('usr_page.html')


@matches.route("/room/<int:room_id>")
@login_required
def show_room(room_id):
    room = Room.query.get(room_id)
    return render_template('match_page.html', room=room)
