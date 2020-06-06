from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from app.matches.func import Editor
from app.matches.forms import *
from app.models import Room, UserRoom
from app import db

matches = Blueprint('matches', __name__)
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
            room_id = editor.create_room(current_user, form.name.data, form.start_time.data,
                               form.max_num_of_player.data, form.game_options.data,
                               form.host_message.data)  # возвращает false если слишком много созданных комнат, добавлю уведомление если фолз, если успею

        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('matches.show_room', room_id=room_id))

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
    return redirect(url_for('matches.user_page'))


@matches.route("/excludeuser/<int:user_id>/<int:room_id>")
@login_required
def exclude_user(user_id, room_id):
    room = Room.query.get(room_id)
    if current_user.id == room.host.id:
        UserRoom.query.filter_by(user_id=user_id, room_id=room.id).delete()
        db.session.commit()
    return redirect(url_for("matches.show_room", room_id=room.id))


@matches.route("/userpage")
@login_required
def user_page():
    rooms = current_user.rooms
    user_rooms = current_user.user_rooms
    return render_template("usr_page.html", rooms=rooms, user_rooms=user_rooms)


@matches.route("/room/<int:room_id>")
@login_required
def show_room(room_id):
    room = Room.query.get(room_id)
    if room_id:
        return render_template('match_page.html', room=room)
    else:
        return redirect(url_for('matches.user_page'))
