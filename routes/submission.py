from flask import Blueprint, jsonify, request
from models import db, Submission

submission_bp = Blueprint('submission', __name__)

@submission_bp.route('/', methods=['POST'])
def submit_project():
    data = request.json
    submission = Submission(user_id=data['user_id'], repo_link=data['repo_link'], loom_link=data['loom_link'], status='Pending')
    db.session.add(submission)
    db.session.commit()
    return jsonify(submission.as_dict()), 201

@submission_bp.route('/<int:submission_id>', methods=['PUT'])
def update_submission(submission_id):
    submission = Submission.query.get_or_404(submission_id)
    data = request.json
    submission.status = data.get('status', submission.status)
    submission.feedback = data.get('feedback', submission.feedback)
    db.session.commit()
    return jsonify(submission.as_dict())

