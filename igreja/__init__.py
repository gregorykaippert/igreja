from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///igreja.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://banco_igrejaesposende_user:U00un7b0PEDy8L277Nzf8AYg3K3v4lTZ@dpg-d9pqoiajnfac73a84f90-a.oregon-postgres.render.com/banco_igrejaesposende"
app.config['SECRET_KEY'] = 'a87bdb321fdce572c1117abbe01d0bd1'

database = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

bcrypt = Bcrypt(app)

from igreja import routes