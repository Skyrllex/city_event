# City Event - Django REST API event platform

## Implemented Functionality
- Full CRUD for events and venues
- Image system with automatic preview generation (200px WebP)
- Access rights management (superuser/regular users)
- Pagination, sorting, and filtering of events
- Search by name and venue
- REST API with Swagger documentation
- Docker containerization
- Weather module

## Extensible Architecture:
- Models prepared for Celery tasks
- Import/export system (basic framework)

## requirements
```
asgiref==3.11.0
Django==6.0.1
django-filter==25.2
djangorestframework==3.16.1
pillow==12.1.0
sqlparse==0.5.5
tzdata==2025.3
pytest==9.0.2
pytest-django = 4.11.1
pytest-cov = 7.0.0
```

## RUN
###  Clone project
```bash
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
You can run cmd
```
python manage.py test apps
```
or run pytest
```bash
pytest --tb=short
```
Run with coverage measurement
```bash
pytest --cov=apps --cov-report=term-missing
pytest --cov=apps --cov-report=html
```
### Run project
```
python manage.py runserver
```
>Open pages in browser
```
http://127.0.0.1:8000/events/list
```
## Docker
> If u install docker
```bash
docker-compose build
docker-compose up
```

### Key generation
### Method 1. Django

## SECRET_KEY 
> Create in main folder SECRET_KEY.env and PUSH KEY

### Key generation
### Method 1. Django
```
venv\Scripts\activate
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


