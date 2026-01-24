# City Event - Django REST API event platform

## Implemented
- DRF (Django REST Framework)
- CRUD (Create, Read, Update, Delete)
- Pagination
- Pillow 
- Tests
- Search, Sort Events

## In process
- User Interface
- Filter 
- Sheldure
- Email notification
- Weather service
- API Documentatiom
- Docker deployment


## requirements
```
asgiref==3.11.0
Django==6.0.1
django-filter==25.2
djangorestframework==3.16.1
pillow==12.1.0
sqlparse==0.5.5
tzdata==2025.3
```

## RUN
###  Use this cod in bash
```
git clone https://github.com/Skyrllex/city_event
cd city_event
python -m venv venv
```
### Start venv:

> Windows
```
venv\Scripts\activate 
```
> Linux : 
```
source venv/bin/activate  
```
### install requirements
```
pip install --upgrate pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```
### USE TEST
```
python manage.py test apps
```
### Run project
```
python manage.py runserver
```


## SECRET_KEY 
> Create in main folder SECRET_KEY.env and PUSH KEY
### Key generation
### Method 1. Django
```
venv/Scripts/Activate
python manage.py shell -c "from django.core.> management.utils import get_random_secret_key; print(get_random_secret_key())"
```
### Method 2. Python
```
python -c "import secrets; print(secrets.token_urlsafe(50))"
```
### Method 3. Test key 
```
django-insecure-test-key-for-development-only-!@#$%^&*()12345
```


