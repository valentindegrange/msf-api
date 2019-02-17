# msf-api
---
REST API to build MSF Roster of Characters - With authentication  
Built with [Python 3.7](https://www.python.org/downloads/) / [Django 2.1](https://www.djangoproject.com/download/) / [django-restframework 3.9](https://www.django-rest-framework.org/#installation)

## Installation
### Python and VirtualEnv
[Download](https://www.python.org/downloads/) and [Install](https://realpython.com/installing-python/) Python 3.7  
Working with [virtualenv](https://virtualenv.pypa.io/en/latest/installation/) is strongly advised.  
Using [virtualenv-wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) is a plus.  
> If you're using virtualenv-wrapper and multiple python instances, you can specify your python version with `mkvirtualenv {your_env} --pyton /your/path/to/python`

### Database
This project uses [PostgreSQL](https://www.postgresql.org/download/)  

### Environment Variables
In order to ease up development here's the different en variables that are set for the project:
```bash
export PROJECT_PATH='/Users/admin/projects/perso/msf-api'
export DB_NAME='msf'
export DB_HOST='127.0.0.1'
export DB_USER='admin'
export DB_PASSWORD=''

# optional but useful aliases, can/should be personalized
alias manage='$PROJECT_PATH/msf/manage.py'
alias runserver='manage runserver'
alias migrate='manage migrate'
alias makemigrations='manage makemigrations'
alias reset_db='dropdb $DB_NAME && createdb $DB_NAME'
```
_Note: if you're using a virtual env, I've set these env var/aliases into `~/.virtualenvs/{my_virtual_env}/bin/activate`_

### Installing the project locally

_Using the different aliases in order to ease up this part. If you have not set them please refer to the Environment Variable part_

- _For mkvirtualenv users: go into your virtual env: `workon {my_virtual_env}`_
- Install the requirements (into the repository `msf-api`): `pip install -r requirements.txt`
- Create the postgres database: `createdb $DB_NAME` 
- _(Optional) You might need to create a superuser before creating your postgres db: `createuser $DB_USER -s`_
- Migrate your database: `manage migrate`
- Create a Django superuser: `manage createsuperuser`

That's it! Your project is ready to be run

### Optional: Pre-populate Database
You can pre-populate your db with: `manage runscript scripts.populate_characters`.  
It will read the json file available into `msf/data/data.json` and create or update your db

## Run the project

In order to run this project, once the installations steps are successfully done, you just need to run `manage runserver`.
It will create a local server at `127.0.0.1:8000` and you will be able to access the API or the Admin console

### API
The API is meant to be reached by any authenticated user.  
It can be reached at `127.0.0.1:8000/api`  

Here an authenticated user can only update his different `CharacterInstance` objects and his `Roster`.  
He can access in Read Only mode the other resources (`Character`, `Trait`, `Material`, ...)

### Admin console
The admin console is meant to be available only for `superuser` or `staff` Users.  
It can be reached at `127.0.0.1:8000/admin`  

Here an authorized user can directly update the `Character`, `Trait`, `Material`, ... objects