
import os
from flask import Flask
from flask_bcrypt import Bcrypt



app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

bcrypt = Bcrypt(app)

from nfl import routes