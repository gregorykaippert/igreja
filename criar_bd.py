from igreja import database, app
from igreja.models import User, Members

with app.app_context():
    # database.drop_all()
    database.create_all()