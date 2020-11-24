import os, traceback
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from datetime import date
from reservation import ResaForm
from contact import ContactForm

app = Flask(__name__)
mail = Mail(app)

app.config['SECRET_KEY'] = os.urandom(32)
app.config["MAIL_SERVER"] = os.environ.get('MAIL_SERVER')
app.config["MAIL_PORT"] = os.environ.get('MAIL_PORT')
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get('MAIL_DEFAULT_SENDER')
app.config["MAIL_RECIPIENT"] = os.environ.get('MAIL_RECIPIENT')
app.config['RECAPTCHA_USE_SSL'] = os.environ.get('RECAPTCHA_USE_SSL')
app.config['RECAPTCHA_PUBLIC_KEY'] = os.environ.get('RECAPTCHA_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ.get('RECAPTCHA_PRIVATE_KEY')
app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}
mail = Mail(app)

@app.route("/")
def index():
        return render_template('index.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    error = None
    contact = ContactForm()
    if request.method == 'POST':
        if not contact.validate():
            error = 'Veuillez remplir tous les champs.'
            return render_template('contact.html', contact=contact)

        else:
            msg = Message("MESSAGE DE {}".format(contact.nom.data), recipients=[os.environ.get('MAIL_RECIPIENT')])
            msg.body = "Nom : {} \nMail : {} \nMessage : {}".format(contact.nom.data, contact.email.data, contact.message.data)

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
            error = 'Veuillez remplir tous les champs.'
            return render_template('reservation.html', form=form)

        elif form.date.data < date.today():
            error = 'Date correcte requise.'
            return render_template('reservation.html', form=form, error=error)

        elif form.heurefin.data < form.heuredebut.data:
            error = 'Veuillez specifier un creneau horaire correct.'
            return render_template('reservation.html', form=form, error=error)

        elif form.heuredebut.data == '':
            error = 'Heure de début requise.'
            return render_template('reservation.html', form=form, error=error)

        elif form.mindebut.data == '':
            error = 'Heure de début requise.'
            return render_template('reservation.html', form=form, error=error)

        elif form.heurefin.data == '':
            error = 'Heure de fin requise.'
            return render_template('reservation.html', form=form, error=error)

        elif form.minfin.data == '':
            error = 'Heure de fin requise.'
            return render_template('reservation.html', form=form, error=error)

        else:
            msg = Message("DEMANDE RESA DE {}".format(form.nom.data), recipients=[os.environ.get('MAIL_RECIPIENT')])
            msg.body =  "Nom : {} \n " \
                        "Mail : {} \n " \
                        "Date : {} \n " \
                        "Heure de début : {} h {}\n " \
                        "Heure de fin : {} h {}\n " \
                        "Nombre de personnes : {}\n " \
                        "Commentaire : {}".format(form.nom.data, form.email.data, form.date.data, form.heuredebut.data, form.mindebut.data, form.heurefin.data, form.minfin.data, form.nbpersonnes.data, form.commentaire.data)

            try:
                mail.send(msg)
            except TypeError as e:
                traceback.print_exc()
                return render_template('reservation.html', success=False)

            return render_template('reservation.html', success=True)

    elif request.method == 'GET':
        return render_template('reservation.html', form=form)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
