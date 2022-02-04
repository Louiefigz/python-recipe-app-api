# python-recipe-app-api

Build Docker Comose Command: 

```
docker-compose build
```


RUN TESTS COMMAND: 
```
docker-compose run app sh -c "python3 manage.py test && flake8"
```

MAKE MIGRATIONS:

```
docker-compose run app sh -c "python3 manage.py makemigrations core"
```
