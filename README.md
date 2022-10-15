# Club Musique ESIEE Web

Site web et application de réservation du studio du Club Musique de l'ESIEE Paris.

## TODO
- [X] Update python and base app
- [x] Review and harden flask app
- [X] Update web app (jquery, bootstrap...)
- [] Minors CSS fix

## Prérequis
### SMTP
Il est nécéssaire de disposer d'un serveur SMTP.

### Captcha
Il est nécéssaire de disposer d'un compte Google afin de générer les clés d'API pour utiliser le Captcha lors de la soumission du formulaire de réservation.

## Installation
### Env
Remplir les variables d'environnement à l'aide des informations demandées

### Docker
Lancer le container Docker sur le serveur cible.

```sh
docker-compose up -d
```