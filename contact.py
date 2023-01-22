from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, SubmitField, validators, StringField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    nom = StringField([validators.DataRequired(message = (u'Nom et Prenom requis')), validators.Length(min=3, message=(u'Votre nom doit comporter plus de 3 lettres.'))])
    email = StringField([validators.DataRequired(message = (u'Adresses mail requise')), validators.Email(u'Adresse mail correcte requise')])
    message = TextAreaField()
    recaptcha = RecaptchaField()
    envoyer = SubmitField()