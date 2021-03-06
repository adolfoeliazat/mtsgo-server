# MTSGO Server
![Build Status](https://travis-ci.org/aneutron/mtsgo-server.svg?branch=master)
![Code Coverage](https://codecov.io/github/aneutron/mtsgo-server/coverage.svg?branch=master)

## Présentation

Ceci est le repo du bloc serveur de l'application MTSGO. Il regroupe le code, la documentation, et les spécifications techniques.

## Dépendences

Pour le moment, le développement se fait avec Python 3, et est testé avec les versions 3.5 et 3.6. _(Des efforts sont en cours pour étudier la portabilité de la solution à Python 2.7)_

Vous pouvez utiliser __SQLite, MySQL,__ ou __PostgreSQL__. Les tests d'intégration sont éxecutés pour tout ces SGBD, et donc tant que vous voyez que le build est en _passing_, cette version de l'application devrait marcher avec les trois.

Le projet dépend des librairies:
- Django (1.10): Framework de base pour le projet
- django-tokenapi (0.2.5): Librairie pour l'authentification
- matplotlib (1.5.3): Utilisé pour résoudre le problème _point in polygon_.
- pymysql (0.7.10): Si vous voulez utiliser MySQL, Le driver classique MySQLdb ne marche pas sur Python 3 pour le moment, c'est pourquoi cet alternative est utilisée. (Elle peut être installée comme si elle était MySQLdb avec du monkey patching) 
- pycopg2: Si vous utilisez PostgreSQL.

## Installation

### Pour votre environnement de développement :

D'abord positionnez vous dans le dossier que vous souhaitez, et cloner le projet:

`git clone https://github.com/aneutron/mtsgo-server`

Ensuite installez les dépendances _(Préférablement dans un __environnement virtuel__ pour éviter les conflits de dépendances)_:

`pip install -r requirements.txt`

Eventuellement modifiez les paramètres dans `mtsgo/settings.py`, ensuite appliquez les schémas à votre BDD avec `python mtsgo-server/manage.py makemigrations` puis `python mtsgo-server/manage.py migrate`.

Pour lancer votre serveur de test, éxecutez:

`python manage.py runserver`

> Astuce: Utilisez [Postman](https://www.getpostman.com/apps) pour accélerer votre développement et vos tests.

### Pour du déploiement :

Il est recommandé d'utiliser [l'image Docker](./Dockerfile) pour setup rapidement une instance pré-configuré. Après avoir installé Docker, il suffit d'éxecuter la commande suivante dans le dossier du repo cloné:

`docker build -f ./Dockerfile -t mtsgo:latest ./`

Et puis:

`docker run -d -p 8080:80 -n mtsgo-server mtsgo:latest`

Vous pouvez alors accéder à votre serveur sur localhost:8080.

> Si votre setup requiert une persistence, monter la base de donnée en volume Docker, ou utiliser une base de donnée MySQL/PgSQL est recommandé.

## Code coverage & Tests

Pour tester la conformité à la spécification de l'API, et assurer une qualité du code assez correcte, des tests ont été écrit pour chaque API
_(mtsgo/test.py, api/test.py, superapi/test.py)_ , et sont lancés automatiquement à chaque _commit_, et des statistiques de code coverage sont générés.

Vous pouvez visiter [la page du projet](https://travis-ci.org/aneutron/mtsgo-server/) sur la plateforme d'intégration continue TravisCI, et aussi [la page du projet](https://codecov.io/gh/aneutron/mtsgo-server/) sur la plateforme de statistiques de code coverage CodeCov.io .

Voici un des graphes montrant la couverture avec l'arborescence du projet:
![Code Coverage Tree](https://codecov.io/gh/aneutron/mtsgo-server/branch/master/graphs/icicle.svg)

## Auteurs

François Beugin, Ronan Garet, Ayoub Boudhar.
