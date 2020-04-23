from flask import request, redirect, url_for
from flask_login import current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


class AdminMix:
#    def is_accessible(self):
#        return current_user.IsAdmin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('users.login', next=request.url))


class AdminView(AdminMix, ModelView):
    pass


class HomeAdminView(AdminMix, AdminIndexView):
    pass