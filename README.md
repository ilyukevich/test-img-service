# test-img-service

- Django 3.2.5
- Django Rest Framework 3.12.4
- Celery 5.1.2 
- Redis 3.5.3

# INSTALL (for linux)

1) Install docker, docker-compose:
2) Git clone https://github.com/ilyukevich/test-img-service.git
3) Execute from the project folder:
```
sudo docker-compose up -d --build
```
4) Enter in container django:
```
sudo docker exec -it django bash
```
- Preparation of migrations:
```
python manage.py makemigrations
```
- Applying migrations:
```
python manage.py migrate
```
- Load data into database. Creating groups and permissions for them, creating superuser, creating users and selecting groups for them:
```
python manage.py load_data_into_database
```
- Collection of all statics:
```
python manage.py collectstatic
```
- Start celery:
```
celery -A config worker -l INFO
```
Start all containers. Use the key -d to run containers in the background:
```
sudo docker-compose up
```
Stop all containers:
```
sudo docker-compose stop
```

### Authorization 
- role superuser - [admin: admin]
- role administrator - [administrator: administrator]
- role user - [user: user]

### Celery 
- task. Sent email for user after success registration: http://localhost/api/registrations/

### Project available:
#### http://localhost/admin

## DRF
#### http://localhost/api/
#### http://localhost/api/token/ - token
#### http://localhost/api/token/refresh/ - refresh token
#### http://localhost/api/registrations/ - registration
#### http://localhost/api/login/ - login
#### http://localhost/api/logout/ - logout
#### http://localhost/api/reset-password/ - reset password

## Swagger:
#### http://localhost/swagger/

## Redoc:
#### http://localhost/redoc/
