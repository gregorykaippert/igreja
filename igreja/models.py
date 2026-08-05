# tabelas do banco de dados

from igreja import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nickname = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    created_at = database.Column(database.DateTime, nullable=False, default=datetime.now())
    admin = database.Column(database.Integer, nullable=False, default=0)
    responsable = database.relationship("Members",
                                        backref='resp',
                                        lazy=True) # responsable for registering the member


class Members(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    full_name = database.Column(database.String, nullable=False)
    birth_date = database.Column(database.DateTime, nullable=False, default=datetime.now())
    since_member = database.Column(database.DateTime,
                                   nullable=False,
                                   default=datetime.now()) # Member since when ?
    email = database.Column(database.String, nullable=False)
    cellphone = database.Column(database.String, nullable=False)
    address = database.Column(database.String, nullable=False)
    place_church = database.Column(database.String, nullable=False) # qual igreja, ex: Barcelos or Esposende
    created_by = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)