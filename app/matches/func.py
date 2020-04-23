from app.models import Room
#from app import db


class Editor:
    def __init__(self, db):
        self.db = db

    def _add_entity(self, entity):
        self.db.session.add(entity)
        self.db.session.commit()

    def create_room(self, room):
        pass

    def edit_room(self, room):
        pass

    def delete_room(self, room):
        pass




