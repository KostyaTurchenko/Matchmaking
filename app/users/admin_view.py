from flask import request, redirect, url_for
from flask_login import current_user, mixins
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


class AdminMix:
    def is_accessible(self):
        try:
            return current_user.is_admin
        except Exception as e:
            print(e)
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('users.login', next=request.url))


class AdminView(AdminMix, ModelView):
    pass


class HomeAdminView(AdminMix, AdminIndexView):
    pass