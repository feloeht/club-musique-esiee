from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, SelectField, SubmitField, validators, StringField, DateField
from wtforms.validators import DataRequired
from datetime import date

HEUREDEBUT = [('', 'De *'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('00', '00')]
HEUREFIN = [('', 'À *'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('00', '00')]
MINCHOIX = [('', 'Min *'), ('00', '00'), ('15', '15'), ('30', '30'), ('45', '45')]
NBPERSONNES = [('', 'Participant(s) *'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5+', '5 ou +')]

class ResaForm(FlaskForm):
    nom = StringField([validators.DataRequired(message = (u'Nom et Prenom requis')), validators.Length(min=3, message=(u'Votre nom doit comporter plus de 3 lettres.'))])
    email = StringField([validators.DataRequired(message = (u'Adresses mail requise')), validators.Email(u'Adresse mail correcte requise')])
    date = DateField(default=date.today, format="%d/%m/%Y")
    heuredebut = SelectField(choices=HEUREDEBUT)
    mindebut = SelectField(choices=MINCHOIX)
    heurefin = SelectField(choices=HEUREFIN)
    minfin = SelectField(choices=MINCHOIX)
    nbpersonnes = SelectField(choices=NBPERSONNES)
    commentaire = TextAreaField('')
    recaptcha = RecaptchaField()
    envoyer = SubmitField('')