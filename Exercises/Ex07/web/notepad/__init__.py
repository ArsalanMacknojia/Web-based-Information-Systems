import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", secret_key)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///site.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from notepad import routes
