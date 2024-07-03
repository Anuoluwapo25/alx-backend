#!/usr/bin/env python3
"""
Basic flask setup
"""


from flask import Flask, request, session
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)

# Mock user settings for demonstration
users = {
    'user1': {'preferred_locale': 'fr', 'preferred_timezone': 'Europe/Paris'},
    'user2': {'preferred_locale': 'en', 'preferred_timezone': 'America/New_York'},
}

# Simulated function to get current user id
def get_current_user_id():
    # This function should return the current logged-in user's ID
    # For demonstration purposes, we are hardcoding a user
    return 'user1'  # change this value to 'user2' to test different users

# Function to get a user's preferred locale
def get_user_preferred_locale(user_id):
    """
    user = users.get(user_id)
    """
    if user:
        return user.get('preferred_locale')
    return None

# Function to get a user's preferred timezone
def get_user_preferred_timezone(user_id):
    user = users.get(user_id)
    if user:
        return user.get('preferred_timezone')
    return None

@babel.localeselector
def get_locale():
    """
    Check URL parameters
    """
    url_locale = request.args.get('lang')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # Check user settings
    user_id = get_current_user_id()
    user_locale = get_user_preferred_locale(user_id)
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    # Check request header
    header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']

@babel.timezoneselector
def get_timezone():
    """
    Check URL parameters
    """
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)  # Validate timezone
            return url_timezone
        except UnknownTimeZoneError:
            pass

    # Check user settings
    user_id = get_current_user_id()
    user_timezone = get_user_preferred_timezone(user_id)
    if user_timezone:
        try:
            pytz.timezone(user_timezone)  # Validate timezone
            return user_timezone
        except UnknownTimeZoneError:
            pass

    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def index():
    return f"Current locale: {get_locale()}, Current timezone: {get_timezone()}"

if __name__ == '__main__':
    app.run(debug=True)

