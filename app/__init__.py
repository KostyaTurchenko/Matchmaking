from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt
#from flask_bcrypt import Bcrypt
#from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
#migrate = Migrate(app, db)
#bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from app.main.routes import main
from app.users.routes import users
from app.matches.routes import matches

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(matches)


# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)
#
#     db.init_app(app)
#     migrate.init_app(app, db)
#     login_manager.init_app(app)
#     bcrypt.init_app(app)
#
#     from app.main.routes import main
#     from app.users.routes import users
#     app.register_blueprint(main)
#     app.register_blueprint(users)
#
#     return app



