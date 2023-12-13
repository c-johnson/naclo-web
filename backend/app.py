from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt, check_password_hash

from functools import wraps

from models import db, User
from functions import verify_login

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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def requires_role(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                # Redirect to login or unauthorized page
                pass
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Application routes
@app.route('/dashboard')
@login_required
def dashboard():
    # Based off of current_user.role, redirect to the appropriate dashboard
    pass

@app.route('/admin-dashboard')
@login_required
@requires_role('Administrator')
def admin_dashboard():
    # Admin dashboard logic
    pass

@app.route('/student-dashboard')
@login_required
@requires_role('Participant')
def student_dashboard():
    # Student dashboard logic
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))  # or your dashboard route

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))  # Redirect to the next page or index
        else:
            flash('Invalid username or password')

    return render_template('login.html')  # Create a login.html template

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
    return 'Welcome to the protected area, ' + current_user.username

# @app.route('/')
# def welcome():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(port=9000)