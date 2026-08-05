from igreja import database, app
from igreja.models import User, Members

with app.app_context():
    database.create_all()