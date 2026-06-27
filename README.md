# RESTful E-commerce API

A production-ready RESTful E-commerce API built with **Django** and **Django REST Framework**.

## Features

* JWT Authentication (SimpleJWT & Djoser)
* Product & Category Management
* Order Management
* Search, Filtering & Ordering
* Redis Caching
* Celery Background Tasks
* PostgreSQL / SQLite Support
* OpenAPI Documentation
* Swagger UI & ReDoc

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL / SQLite
* Redis
* Celery
* SimpleJWT
* Djoser
* django-filter
* drf-spectacular

## Installation

```bash
git clone https://github.com/yourusername/restful-ecommerce-api.git
cd restful-ecommerce-api

python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Documentation

* Swagger UI: `/api/schema/swagger-ui/`
* ReDoc: `/api/schema/redoc/`

## License

This project is for learning and portfolio purposes.
