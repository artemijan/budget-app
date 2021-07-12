# budget-app

## requirements

- python 3.9
- virtualenv
- pip
- docker
- docker-compose

## initial setup

```shell
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up -d
python manage.py runserver
```

## to create a superuser

```shell
python manage.py createsuperuser
```

and follow script instructions

## to load test data

```shell
python manage.py loaddata fixtures/test.json
```
