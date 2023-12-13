from app import app
from models import db, User
from functions import register_admin

if __name__ == "__main__":
    with app.app_context():
        register_admin('chris@cjohnson.io', 'gorditasupreme')