# from run import app
from app import app
from app.functions import register_admin

if __name__ == "__main__":
    with app.app_context():
        register_admin('blueberry', 'muffin')