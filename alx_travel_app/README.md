# alx_travel_app_0x01

## Overview

Django REST API for managing Listings and Bookings.

## Endpoints

- `/api/listings/` : CRUD for Listings
- `/api/bookings/` : CRUD for Bookings
- `/swagger/` : API documentation

## Usage

1. Run migrations:

   ```bash
   python manage.py migrate
   ```

2. Start the server:

   ```bash
   python manage.py runserver
   ```

3. Visit:
   - `http://localhost:8000/api/listings/`
   - `http://localhost:8000/api/bookings/`
   - `http://localhost:8000/swagger/`

## Tools

- Django REST Framework
- drf-yasg for Swagger
- Postman/Swagger UI for testing
