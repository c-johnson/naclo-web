from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from flask_bcrypt import check_password_hash

from functools import wraps

from app import app, login_manager
from app.functions import verify_login
from app.models import User

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