# Finance API

This finance API contains the following endpoints:

- User register.
- User login.
- Restaurants list based on his city or latitude and longitude for logged users.
- Historical user transactions.
- User logout.

## Architecture

![Architecture](https://user-images.githubusercontent.com/31974084/184745208-734405e7-8556-4054-8207-b98e9093daf0.png)

## Technologies

The used technologies were:

- **FastAPI:** It's a web framework for building APIs in Python with high performance and ready for production (https://fastapi.tiangolo.com).
- **PostgreSQL:** It's a powerful object-relational database (https://www.postgresql.org).
- **Redis:** It's an in-memory data structure store, used as a distributed in-memory key-value database, cache and message broker (https://redis.io).
- **Docker:** It's an ecosystem for building, deploying and managing containerized applications (https://www.docker.com).
- **Docker Compose:** It's a tool for defining and running multi-container Docker applications (https://docs.docker.com/compose).
- **Psycopg Binary:** It's an adapter that allows you connect to PostgreSQL server and access to the tools that it offers (https://pypi.org/project/psycopg-binary).
- **PyJWT:** It's JSON Web Token implementation in order to secure the APIs using different type of encryption algorithms (https://pypi.org/project/PyJWT).
- **Pytest:** It's a framework to test the applications and it can run **unit** and **integration** tests (https://docs.pytest.org/en/7.1.x).
- **Coverage:** It's a tool to measure code coverage during test execution (https://pypi.org/project/coverage).
- **Black:** It's a tool to format and have a good understading of the code. It uses **PEP8** as its standard styles guide (https://pypi.org/project/black).
- **Flake8:** It's a tool to lint and have good coding practices. It also uses **PEP8** as its standard styles guide (https://pypi.org/project/flake8).

## Environment variables

These environment variables must be set before running the application.

- **ENV**: Environment where the application will be executed, e.g **production**.
- **URL**: URL where the application is running, e.g **http://localhost:8000**.
- **POSTGRES_HOST**: Database host, e.g **localhost**.
- **POSTGRES_PORT**: Database port, e.g **5432**.
- **POSTGRES_SCHEMA**: Database name
- **POSTGRES_USER**: Database user.
- **POSTGRES_PASSWORD**: Database password.
- **REDIS_HOST**: Redis host, e.g **localhost**.
- **REDIS_PORT**: Redis port, e.g **6379**.
- **REDIS_PASSWORD**: Redis password.
- **JWT_PRIVATE_KEY**: Private RSA key used for JWT token encoding.
- **JWT_PUBLIC_KEY**: Public RSA key used for JWT token decoding.
- **TRAVEL_ADVISOR_API_URL**: External API URL used for getting restaurants in the world.
- **TRAVEL_ADVISOR_API_KEY**: External API KEY used for endpoint calls.
- **TRAVEL_ADVISOR_HOST**: Host used for the external API headers.

## Execution

You can run this application with the following command:

```bash
$ docker-compose up
```

## Testing

Some unit tests were implemented in order to check the finance API services. You can run them and see the coverage report with the following commands:

```bash
$ python3.10 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade -r requirements.txt
$ coverage run -m pytest --verbose
$ coverage report -m
```
