from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'maria_eduarda_martins_do_nascimento14'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.view import homepage
from app.models import Contato