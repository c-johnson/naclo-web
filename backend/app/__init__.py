from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt, check_password_hash

from app.models import db

# Initial app instantiation
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://naclolocal:naclopass@localhost/naclodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8c031b18ba3d06c8d033ea60'  # Replace with your secret key

# Database and migration initialization
db.init_app(app)
migrate = Migrate(app, db)

# Admin panel instantiation
admin = Admin(app, name='MyApp', template_mode='bootstrap3')

# Flask-login code; loaders, role decorators, login manager, bcrypt initialization
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

bcrypt = Bcrypt(app)

from app import routes