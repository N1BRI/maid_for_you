from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flask import current_app as app
from flask_wtf import FlaskForm
from werkzeug.exceptions import abort
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import extensions
from forms import ContactForm
bp = Blueprint('home', __name__)



@bp.route('/')
def index():
    return render_template('index.html', form=ContactForm())

@bp.route('/submit', methods=['GET', 'POST'])
def submit_quote():
    print(request.form)
    # Usage
    # subject = "New Quote Request"
    # # body = "{}\nYou have a new request for a quote:\nName: {}\nPhone: {}\nHow did They Hear About Us?: {}\nProperty Type: {}\nSpecfic Areas or Requests: {}\nComments: {}I".format(datetime.now(), request.form['full_name'], request.form['phone'], heard_about[int(request.form['heard_about'])], property_type[int(request.form['property_type'])], request.form['special_attention'], request.form['other_message'])
    # to_email = "n1bri@tuta.io"
    # #to_email = "maid4youhk@yahoo.com"
    # from_email = "maid4uct@gmail.com"
    # password =  app.config.get("GMAIL")

    # send_email(subject, body, to_email, from_email, password)
    form = ContactForm(request.form)
    if extensions.hcaptcha.verify() and form.validate_on_submit():
        # Process form data
        flash("Form submitted successfully! We'll be in touch shortly!", 'success')
        return redirect(url_for('home.index'))
    return render_template('index.html', form=form, scroll_to="#contact-form")


def send_email(subject, body, to_email, from_email, password):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and start TLS encryption
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to your email account
        server.login(from_email, password)

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        # Quit the SMTP server
        server.quit()
