## Technology stack

- Backend: Django
- Database: PostgreSQL

## Backend

```plaintext

Example .env file
DATABASE_NAME = db_name
DATABASE_USER = user
DATABASE_PASSWORD = password
DATABASE_HOST = localhost
DATABASE_PORT = 5432
```

#### First, create and activate venv

```sh
python -m venv venv
```
#### Activate venv

Linux
```sh
source venv/bin/activate
```
Windows
```sh
venv/scripts/activate
```

#### Install Poetry

```sh
pip install poetry
```

#### Installing packages

```sh
poetry install
```

### To run a Django server

#### Set migrations

```sh
python manage.py makemigrations
```

#### Apply Migrations

```sh
python manage.py migrate
```

#### Run server

```sh
python manage.py runserver
```

### Also you can just run docker-compose file

```sh
docker-compose up
```
