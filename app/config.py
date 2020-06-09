import os


class Config:
    SECRET_KEY = '908b462bed32727f9f094087bd0f99ed'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    print(SQLALCHEMY_DATABASE_URI)