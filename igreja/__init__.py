from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///igreja.db'
app.config['SECRET_KEY'] = 'a87bdb321fdce572c1117abbe01d0bd1'

database = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

bcrypt = Bcrypt(app)

from igreja import routes