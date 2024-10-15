from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

from routes.auth import auth_bp
from routes.lesson import lesson_bp
from routes.submission import submission_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(lesson_bp, url_prefix='/lessons')
app.register_blueprint(submission_bp, url_prefix='/submissions')

if __name__ == '__main__':
    app.run(debug=True)

