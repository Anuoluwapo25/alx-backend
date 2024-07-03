#!/usr/bin/env python3
"""
Basic flask setup
"""


from flask import Flask, request, session
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = ['en', 'fr']

babel = Babel(app)

# Mock user settings for demonstration
users = {
    'user1': {'preferred_locale': 'fr'},
    'user2': {'preferred_locale': 'en'},
}

# Simulated function to get current user id
def get_current_user_id():
    # This function should return the current logged-in user's ID
    # For demonstration purposes, we are hardcoding a user
    return 'user1'  # change this value to 'user2' to test different users

# Function to get a user's preferred locale
def get_user_preferred_locale(user_id):
    user = users.get(user_id)
    if user:
        return user.get('preferred_locale')
    return None

@babel.localeselector
def get_locale():
    # Check URL parameters
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

@app.route('/')
def index():
    return f"Current locale: {get_locale()}"

if __name__ == '__main__':
    app.run(debug=True)

