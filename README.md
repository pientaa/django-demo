# djangoDemo

## Run database
```bash
docker-compose up
```
## Create superuser
```bash
python manage.py migrate
python manage.py createsuperuser      
```

## Apply migrations
```bash
python manage.py makemigrations django_demo
python manage.py migrate
```

## Print migrations
```bash
python manage.py sqlmigrate django_demo 0001
```