# URL Shortener

This is a simple URL Shortener application built with Django. It allows users to shorten long URLs, manage their shortened URLs, and redirect from the shortened URL to the original URL.

## Features

- User authentication
- Create short URLs
- List user-specific short URLs
- Redirect to the original URL using the short URL
- View the auto generated code documentationas full fledged HTML pages using Sphinx
- Generate detailed code coverage reports using pytest

## Requirements

- Python 3.8+
- Django 3.2+
- PostgreSQL
- Docker (optional, for containerized deployment)
- Poetry (for dependency management)

## Installation

### Using Poetry

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bibinshajan12/huqsv-urlshortener.git
   cd urlshortener

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv**
   source venv/bin/activate  
3. **Install Dependencies**

   ```bash
   pip install -r requirments.txt 

4. **Create and update env file**

   ```bash
   Create a .env file for environment variables
    DATABASE_NAME=yourdbname
    DATABASE_USER=yourdbuser
    DATABASE_PASSWORD=yourdbpassword
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
5. **Apply Migrations**
   
   ```bash
   python manage.py migrate
6. **create superuser or use the one already existing for demo**
   
   ```bash
   python manage.py createsuperuser
7. **Run the dev server**
    ```bash
   python manage.py runserver
   
8. **Using Docker**
   ```bash
   1. git clone https://github.com/bibinshajan12/huqsv-urlshortener.git
   2. cd urlshortener
   3. docker-compose up --build or docker-compose up --build --force-recreate
   4. Open your web browser and navigate to http://localhost:8000.
   5. By default the docker creates a admin user name and password, which could be used to login to the application
      username : admin
      pwd : adminpassword
9.  **Running Tests and Generate Coverage Report**
    ```bash
        pytest
        pytest --cov=. --cov-config=.coveragerc --cov-report=html
10. **View Sphinx Documentation**
    ```bash
    once in the application, navigate to the view docs button , this will give a complete know how on the application structure

11. **Project Structure**
    ```bash
        urlshortener/
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── forms.py
            ├── models.py
            ├── tests/
            │   ├── __init__.py
            │   ├── test_forms.py
            │   ├── test_models.py
            │   └── test_views.py
            ├── urls.py
            └── views.py
            manage.py
            docker-compose.yml
            .env.example
