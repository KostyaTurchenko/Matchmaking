from flask import render_template, request, Blueprint, redirect, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from app.users.forms import RegistrationForm, LoginForm
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
admin.add_view(AdminView(models.Genre, db.session))


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return render_template(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        if access.registration(form.username.data, form.email.data, form.password.data):
            flash("Ваш Аккаунт был успешно создан!", "success")
            return redirect(url_for("users.login"))
        else:
            flash("Такой пользователь уже существует!", 'danger')
    return render_template("registration.html", form=form)


@users.route('/', methods=['GET', 'POST'])
@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        if access.login(form.username.data, form.password.data):
            return redirect(url_for("main.home"))
        else:
            flash("Неправильный логин или пароль!", 'danger')
    return render_template("authorisation.html", form=form)
