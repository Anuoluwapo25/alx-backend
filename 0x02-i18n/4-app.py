#!/usr/bin/env python3
"""
create config class for flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    config class for flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    best language match
    """
    supported_locale = app.config['LANGUAGES']
    locale_lang = request.args.get('locale')
    if locale_lang in supported_locale:
        return locale_lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    return 4-index.html
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
