#  1. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#  2. .\venv\Scripts\activate
#  Result: (venv) PS W:\Python\projects\ecommerce_platform>

# -------------------------- Create a Virtual Environment:
# In your main projects folder:     python -m venv venv

# -------------------------- Activate the Environment:
# .\venv\Scripts\activate

# -------------------------- Install Django and Create the Project:
# (venv) pip install django Pillow
# Pillow is needed for ImageField, so we install it now.
# (venv) django-admin startproject platform_project .
# The dot '.' at the end creates the project in the current directory.
# (venv) python manage.py startapp store


# -------------------------- Apply the changes to your database:
# (venv) python manage.py makemigrations
# This creates the migration file (the instructions)
# (venv) python manage.py migrate
# This applies the migration to your database (creates the tables)


# -------------------------- Create a Superuser:
# (venv) python manage.py createsuperuser
# Follow the prompts to set a username, email, and password.


# --------------------------  Run the development server:
# python manage.py runserver
