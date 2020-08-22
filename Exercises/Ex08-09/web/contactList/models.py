from flask_login import UserMixin
from contactList import db, login_manager, app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.username}')"

class Contacts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(16))
    notes = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Contacts('{self.first_name}', '{self.last_name}')"