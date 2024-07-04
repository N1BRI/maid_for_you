import os
import home
import extensions
from flask import Flask



app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['HCAPTCHA_ENABLED'] = os.getenv('HCAPTCHA_ENABLED')
app.config['HCAPTCHA_SITE_KEY'] = os.getenv('HCAPTCHA_SITE_KEY')
app.config['HCAPTCHA_SECRET'] = os.getenv('HCAPTCHA_SECRET')
app.config['GMAIL'] = os.getenv('GMAIL')
    
extensions.init_app(app)

app.register_blueprint(home.bp)
