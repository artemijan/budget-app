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

after that:

- admin site will be available under http://localhost:8000/admin/
- browsable api site will be available under http://localhost:8000/api/

to access thet site you need to create a superuser

## to create a superuser

```shell
python manage.py createsuperuser
```

and follow script instructions

## to load test data

```shell
python manage.py loaddata fixtures/test.json
```

## how to run unit tests

```shell
python manage.py test
```
