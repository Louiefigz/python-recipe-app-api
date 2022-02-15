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

Run the Docker container. It makes the migrations in the DB and spins up the server

```
docker-compose --verbose up
```

