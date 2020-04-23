from flask import render_template, request, Blueprint
from app import app
from app.users.func import Accession
from app.models import *
from flask_admin import Admin
from app.users.admin_view import AdminView, HomeAdminView
from app import models, db

users = Blueprint("users", __name__)
access = Accession(db)

admin = Admin(app, 'App', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(models.User, db.session))
admin.add_view(AdminView(models.Room, db.session))
admin.add_view(AdminView(models.Game, db.session))
admin.add_view(AdminView(models.GameGenre, db.session))



@users.route("/register", methods=['GET', 'POST'])
def register():
    User.query.all()
    return render_template("registration.html")


@users.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("autorisation.html")