from models import db, User, Participant, Administrator
from flask_bcrypt import generate_password_hash, check_password_hash

def register_participant(username, password):
    hashed_password = generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password, role='Participant')
    db.session.add(new_user)
    db.session.commit()

    participant = Participant(user_id=new_user.id)
    db.session.add(participant)
    db.session.commit()

def register_admin(username, password):
    hashed_password = generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password, role='Administrator')
    db.session.add(new_user)
    db.session.commit()

    participant = Administrator(user_id=new_user.id)
    db.session.add(participant)
    db.session.commit()

def verify_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # Password is correct
        login_user(user)
        return True
    else:
        # Password is incorrect
        return False