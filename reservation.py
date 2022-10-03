from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators, StringField, EmailField, DateField, TimeField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired
from datetime import date

NBPERSONNES = [('', 'Participant(s) *'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5+', '5 ou +')]

class ResaForm(FlaskForm):
    nom = StringField(validators = [validators.InputRequired()])
    email = EmailField(validators = [validators.InputRequired(), validators.Email()])
    date = DateField(default=date.today, format="%Y-%m-%d")
    heuredebut = TimeField(validators = [validators.InputRequired()])
    heurefin = TimeField(validators = [validators.InputRequired()])
    nbpersonnes = SelectField(choices=NBPERSONNES, validators = [validators.InputRequired()])
    commentaire = TextAreaField()
    recaptcha = RecaptchaField()
    envoyer = SubmitField()