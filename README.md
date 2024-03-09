# Currency App Backend

API for Currency Management application

![alt text](https://img.shields.io/badge/python-3.10.9-green)

## Development

### Up and build containers
```shell
docker-compose up -d --build
```

### Install poetry
```shell
pip install poetry
```
 
### Install the project dependencies
```shell
poetry install
```

### Spawn a shell within the virtual environment
```shell
poetry shell
```

### Run dev server
```shell
python manage.py runserver
```

### Run tests
```shell
pytest
```

## Start server

### Start dev server
```shell
docker-compose up -d --build

pip install poetry
poetry install
poetry shell

python manage.py runserver
```

### Use via swagger

1. Go to http://localhost:8000/api/docs/
2. After sign_up or sign_in use the token from the response body and place it in the Authorize form with the pattern 

```
Bearer {your_token}
```

3. Use swagger

