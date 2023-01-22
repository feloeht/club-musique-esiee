# Club Musique ESIEE Web

Site web et application de réservation du studio du Club Musique de l'ESIEE Paris.

## Prérequis
### SMTP
Il est nécéssaire de disposer d'un serveur SMTP.

### Captcha
Il est nécéssaire de disposer d'un compte Google afin de générer les clés d'API pour utiliser le Captcha lors de la soumission du formulaire de réservation.

## Installation
### Env

```sh
MAIL_SERVER=YOUR_SERVER
MAIL_PORT=YOUR_PORT
MAIL_USE_SSL=True/False
MAIL_USE_TLS=True/False
MAIL_DEFAULT_SENDER=YOUR_USERNAME
MAIL_RECIPIENT=YOUR_RECIPIENT
RECAPTCHA_USE_SSL=True/False
RECAPTCHA_PUBLIC_KEY=X
RECAPTCHA_PRIVATE_KEY=X
```

### Docker
Lancer le container Docker sur le serveur cible.

```sh
docker-compose up -d
```