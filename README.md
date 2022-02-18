# python-recipe-app-api

Build Docker Comose Command: 

```
docker-compose build
```


RUN TESTS COMMAND: 
```
docker-compose run --rm app sh -c "python3 manage.py test && flake8"
```

MAKE MIGRATIONS:

```
docker-compose run app sh -c "python3 manage.py makemigrations core"
```

Run the Docker container. It makes the migrations in the DB and spins up the server

```
docker-compose --verbose up
```

Run one test example:
docker-compose run app sh -c "python3 manage.py test PublicUserApiTests.test_create_token_for_user && flake8"

Start the Django Shell:

python manage.py shell

Password for Admin: 
email, 
password = Awesome1