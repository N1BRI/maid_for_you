import os
import home
import extensions
from flask import Flask

app = Flask(__name__)


app.config.from_mapping(
    SECRET_KEY='dev',
)

app.config.from_pyfile('config.py', silent=True)
    
extensions.init_app(app)

app.register_blueprint(home.bp)
