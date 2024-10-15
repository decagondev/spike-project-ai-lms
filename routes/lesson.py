from flask import Blueprint, jsonify, request
from models import db, Lesson

lesson_bp = Blueprint('lesson', __name__)

@lesson_bp.route('/', methods=['GET'])
def get_lessons():
    lessons = Lesson.query.all()
    return jsonify([lesson.as_dict() for lesson in lessons])

@lesson_bp.route('/', methods=['POST'])
def add_lesson():
    data = request.json
    lesson = Lesson(title=data['title'], live_lesson_link=data['live_lesson_link'], date=data['date'])
    db.session.add(lesson)
    db.session.commit()
    return jsonify(lesson.as_dict()), 201

