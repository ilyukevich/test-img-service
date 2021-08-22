# test-img-service

- Django 3.2.5
- Django Rest Framework 3.12.4

# INSTALL

1) Git clone https://github.com/ilyukevich/test-img-service.git
2) Execute from the project folder:

```
pip install -r requirements.txt
```
Preparation of migrations:
```
python manage.py makemigrations
```
Applying migrations:
```
python manage.py migrate
```
Load data into database. Creating groups and permissions for them, creating superuser, creating users and selecting groups for them:
```
python manage.py load_data_into_database
```
Server start:
```
 python manage.py runserver
 ```
###Authorization 
- superuser - [admin: admin]
- administrator - [administrator: administrator]
- user - [user: user]

####http://localhost:8000/
####http://localhost:8000/admin

##DRF
####http://localhost:8000/api/
##Swagger:
####http://localhost:8000/swagger/

##Redoc:
####http://localhost:8000/redoc/


# *UPD INSTALL
- install docker, docker-compose
- git clone https://github.com/ilyukevich/test-img-service.git
- from project folder:
```
sudo docker-compose up -d --build
```
- enter in container django:
```
sudo docker exec -it django bash
```
a) from container django. Preparation of migrations:
```
python manage.py makemigrations
```
b) from container django. Applying migrations:
```
python manage.py migrate
```
c) from container django. Load data into database. Creating groups and permissions for them, creating superuser, creating users and selecting groups for them:
```
python manage.py load_data_into_database
```
LOGIN: PASS 
- superuser - admin: admin
- administrator - administrator: administrator
- user - user: user

d) from container django. Collection of all statics:
```
python manage.py collectstatic
```
- start all containers. Use the key -d to run containers in the background:
```
sudo docker-compose up
```
- stop all containers:
```
sudo docker-compose stop
```
- http://127.0.0.1/
- http://127.0.0.1/admin/
- http://localhost/
- http://localhost/admin/

- Swagger:
```
http://localhost/swagger/
```
- Redoc:
```
http://localhost/redoc/
```