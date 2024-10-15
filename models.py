from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(10), nullable=False)
    okta_id = db.Column(db.String(100), unique=True, nullable=False)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    live_lesson_link = db.Column(db.String(200), nullable=False)
    recording_link = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    repo_link = db.Column(db.String(200), nullable=False)
    loom_link = db.Column(db.String(200), nullable=False)
    feedback = db.Column(db.String(500))
    status = db.Column(db.String(20), nullable=False)

