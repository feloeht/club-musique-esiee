import os, traceback
from config import Config
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from datetime import date

app = Flask(__name__)

app.secret_key = os.urandom(32)
app.config.from_object("config.Config")

mail = Mail(app)

from app.src.reservation import ResaForm
from app.src.contact import ContactForm

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/planning")
def planning():
    return render_template('planning.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    error = None
    contact = ContactForm()
    if request.method == 'POST':
        if not contact.validate():
            error = """
            <div class="alert alert-danger d-flex align-items-center" role="alert">
            <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                <div>Merci de renseigner tous les champs.</div>
            </div>
            """
            return render_template('contact.html', contact=contact, error=error)

        else:
            msg = Message("Message de contact de {}".format(contact.nom.data), recipients=[os.environ.get('MAIL_RECIPIENT')])
            msg.body = "Nom : {}\n \
                        Mail : {}\n \
                        Message : {}".format(contact.nom.data, contact.email.data, contact.message.data)

            try:
                mail.send(msg)
            except TypeError as e:
                traceback.print_exc()
                return render_template('contact.html', success=False)

            return render_template('contact.html', success=True)

    elif request.method == 'GET':
        return render_template('contact.html', contact=contact)
        
@app.route("/reservation", methods=['GET', 'POST'])
def reservation():
    error = None
    form = ResaForm()

    if request.method == 'POST':
        if not form.validate():
            error = """
            <div class="alert alert-danger d-flex align-items-center" role="alert">
            <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                <div>Merci de renseigner tous les champs.</div>
            </div>
            """
            return render_template('reservation.html', form=form, error=error)

        elif form.date.data < date.today():
            error = """
            <div class="alert alert-danger d-flex align-items-center" role="alert">
            <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                <div>La date renseignée est antérieure à la date du jour.</div>
            </div>
            """
            return render_template('reservation.html', form=form, error=error)

        elif form.heurefin.data < form.heuredebut.data:
            error = """
            <div class="alert alert-danger d-flex align-items-center" role="alert">
            <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                <div>L'heure de fin renseignée est antérieur à l'heure de début.</div>
            </div>
            """
            return render_template('reservation.html', form=form, error=error)

        else:
            msg = Message("Demande de réservation de {}".format(form.nom.data), recipients=[os.environ.get('MAIL_RECIPIENT')])
            msg.body =  "Nom : {}\n" \
                        "Mail : {}\n" \
                        "Date : {}\n" \
                        "Heure de début : {}\n" \
                        "Heure de fin : {}\n" \
                        "Nombre de personnes : {}\n" \
                        "Motif de la demande : {}\n" \
                        "Commentaire : {}".format(form.nom.data, form.email.data, form.date.data, form.heuredebut.data, form.heurefin.data, form.nbpersonnes.data, form.motif.data, form.commentaire.data)

            try:
                mail.send(msg)
            except TypeError as e:
                traceback.print_exc()
                return render_template('reservation.html', success=False)

            return render_template('reservation.html', success=True)

    elif request.method == 'GET':
        return render_template('reservation.html', form=form)