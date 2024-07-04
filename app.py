import os
import home
from flask import Flask
from flask_hcaptcha import hCaptcha



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['HCAPTCHA_ENABLED'] = os.getenv('HCAPTCHA_ENABLED')
app.config['HCAPTCHA_SITE_KEY'] = os.getenv('HCAPTCHA_SITE_KEY')
app.config['HCAPTCHA_SECRET_KEY'] = os.getenv('HCAPTCHA_SECRET_KEY')
app.config['GMAIL'] = os.getenv('GMAIL')
hcaptcha = hCaptcha(secret_key=os.getenv('HCAPTCHA_SECRET'), site_key=os.getenv('HCAPTCHA_SITE_KEY'))
hcaptcha.init_app(app)
app.config['hcaptcha'] = hcaptcha

app.register_blueprint(home.bp)
