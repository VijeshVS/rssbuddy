from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SECRET_KEY'] = '46d41ac8259358fac094234d'


db = SQLAlchemy(app)
app.app_context().push()

if __name__ == '__main__':
    app.run()

from rssbuddy import routes

