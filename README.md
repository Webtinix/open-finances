# Installation et Configuration de Django

## 1. Créer un environnement virtuel

```bash
python -m venv .env
```

Cette commande crée un environnement virtuel nommé .env dans le répertoire actuel.  

## 2. Mettre à jour pip

```bash
pip install --upgrade pip

python.exe -m pip install --upgrade pip
```

Assurez-vous que pip, l'outil de gestion des paquets de Python, est à la dernière version.

## 3. Installer Django

```bash
pip install django
```

Installe la dernière version de Django dans l'environnement virtuel.

## 4. Générer le fichier de dépendances

```bash
pip freeze > requirements.txt
```

Crée un fichier requirements.txt qui répertorie toutes les dépendances du projet.

## 5. Installer les dépendances depuis le fichier

```bash
pip install -r requirements.txt
```

Installe les dépendances du projet à partir du fichier requirements.txt.

## 6. Créer un projet Django

```bash
django-admin startproject openfinances .
```

Initialise un projet Django nommé "openfinances" dans le répertoire actuel (.).

## 7. Lancer le serveur de développement

```bash
python src/manage.py runserver
```

Démarre le serveur de développement Django. Ouvrez votre navigateur et accédez à http://127.0.0.1:8000/ pour voir votre application.

## 8. Effectuer les migrations

```bash
python src/manage.py migrate
```

Applique les migrations pour créer la base de données.

```bash
python src/manage.py migrate app
``` 

Applique les migrations pour créer la base de données pour une application.

```bash
python src/manage.py sqlmigrate app migatrion_file_name
``` 

Afficher le code SQL de la migration.

## 9. Créer une application Django

```bash
cd src && python manage.py startapp app && cd ..
```

Crée une application Django nommée "app" dans le répertoire src.

## 10. Créer des migrations pour une application spécifique

```bash
python src/manage.py makemigrations app
```

## 11. Création d'un super utilisateur

```bash
python src/manage.py createsuperuser
```

## 12. Django shell

```bash
python src/manage.py shell
```

# Installation et Configuration de Git

## 1. Initialisation du dépôt Git

```bash
git remote add origin https://github.com/Webtinix/open-finances.git
```

Ajout du dépôt distant Git au projet.

```bash
git remote set-url origin https://github.com/Webtinix/open-finances.git
```

Modification du dépôt Git au projet.

## 2. Envoie du code projet (Push) sur le dépôt distant Git

```bash
git add . && git commit -m "your commit" && git push -u origin main
git add . && git commit -m 'your commit' && git push origin
```

```bash
git push --set-upstream origin main -f
```

Pour pousser la branche courante et définir la branche distante comme branche amont.

# Configuration de la base de données PostgreSQL

## 1. Afficher rôle et utilisateur

```bash
\du
```

Affiche tous les utilisateurs et rôles de la base de données.

## 2. Création d'utilisateur 

```bash
CREATE USER user WITH ENCRYPTED PASSWORD 'p@$$w0rd';
```

Créé l'utilisateur **user** dans la base de données et lui attribue le mot de passe **p@$$w0rd**.

```bash
ALTER ROLE user SET client_encoding TO 'utf8';
```

Modification du paramêtre **client_encoding** en **utf8**.

```bash
ALTER ROLE user SET default_transaction_isolation TO 'read committed';
```

Modification du paramêtre **default_transaction_isolation** en **read committed**.

## 3. Liste des bases de données

```bash
\l
```

Lister toutes les bases de données du SGBD.

```bash
CREATE DATABASE bdd;
```

Créer la base de données **bdd**.

```bash
GRANT ALL PRIVILEGES ON DATABASE bdd TO user;
```

Donner tous les droits à l'utilisateur **user** sur la base de données **bdd**.

```bash
ALTER DATABASE bdd OWNER TO user;
```

Définir **user** comme propriétaire de la base de données **bdd**.






https://realpython.com/customize-django-admin-python/
https://docs.djangoproject.com/fr/3.0/topics/forms/modelforms/

https://www.youtube.com/watch?v=cgj4sz0bytk
https://www.youtube.com/watch?v=eosXCVcgtPw

https://docs.djangoproject.com/fr/5.0/topics/pagination/
https://docs.djangoproject.com/fr/5.0/topics/forms/
https://docs.djangoproject.com/fr/5.0/topics/forms/modelforms/#top

https://docs.djangoproject.com/fr/5.0/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin