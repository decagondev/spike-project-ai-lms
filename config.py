import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OKTA_ISSUER = 'https://okta_domain.okta.com'
    OKTA_CLIENT_ID = 'client-id'
    OKTA_CLIENT_SECRET = 'client-secret'

