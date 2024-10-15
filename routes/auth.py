from flask import Blueprint, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from config import Config

auth_bp = Blueprint('auth', __name__)

oauth = OAuth()

okta = oauth.remote_app(
    'okta',
    consumer_key=Config.OKTA_CLIENT_ID,
    consumer_secret=Config.OKTA_CLIENT_SECRET,
    request_token_params={
        'scope': 'openid profile email',
    },
    base_url=Config.OKTA_ISSUER + '/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url=Config.OKTA_ISSUER + '/oauth2/v1/token',
    authorize_url=Config.OKTA_ISSUER + '/oauth2/v1/authorize',
)

@auth_bp.route('/login')
def login():
    return okta.authorize(callback=url_for('auth.callback', _external=True))

@auth_bp.route('/callback')
def callback():
    response = okta.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error'], request.args['error_description']
        )

    session['okta_token'] = (response['access_token'], '')
    return jsonify({"message": "Login successful"})

@auth_bp.route('/logout')
def logout():
    session.pop('okta_token', None)
    return redirect(url_for('auth.login'))

@okta.tokengetter
def get_okta_oauth_token():
    return session.get('okta_token')

