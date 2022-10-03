from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators, StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    nom = StringField(validators = [validators.InputRequired()])
    email = EmailField(validators = [validators.InputRequired(), validators.Email()])
    message = TextAreaField()
    recaptcha = RecaptchaField()
    envoyer = SubmitField()