# comptarcilite
Application web de gestion de compte, permettant de gérer son budget/comptabilité personnelle

## Installation

Exécuter les commandes suivantes pour faire fonctionner le serveur.

```shell
git clone https://github.com/HE-Arc/comptarcilite.git
virtualenv -p python3 demoenv
. demoenv/bin/activate
cd comptarcilite
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```
