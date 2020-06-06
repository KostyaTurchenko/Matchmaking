from app.models import Room, UserRoom
#from app import db


class Editor:
    def __init__(self, db):
        self.db = db

    def _add_entity(self, entity):
        self.db.session.add(entity)
        self.db.session.commit()

    def create_room(self, user, name, start_time, max_num_of_player, game, host_message):
        if len(user.user_rooms) < 5:
            r = Room(name=name, start_time=start_time, max_num_of_player=max_num_of_player,
                     game=game, host_message=host_message, host=user)
            self._add_entity(r)
            return True  # тру фолз, чтобы знать, когда слишком много созданных комнат
        return False

    # def edit_room(self, room):  РЕАЛИЗОВАТЬ В routes!
    #     pass

    def delete_room(self, user, room_id):
        room = Room.query.filter_by(id=room_id)
        if room in user.rooms:
            UserRoom.query.filter_by(room_id=room_id).delete()
            self.db.session.delete(room)
            self.db.session.commit()





