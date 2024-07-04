from flask_hcaptcha import hCaptcha

hcaptcha = hCaptcha()

def init_app(app):
    hcaptcha.init_app(app)