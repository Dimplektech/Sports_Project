
# Django Sports Registration Project

This is a Django-based web application for managing sports registrations. Users can register for sports events, view registered teams, and administrators can manage these registrations.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact]

## Features
- User registration and authentication.
- Different user roles (Admin and Basic).
- Register for sports events.
- View list of registered teams.
- Admins can delete registrations.

## Installation

### Prerequisites
- Python 3.8+
- Django 3.2+
- Virtualenv (optional but recommended)

### Setup

1. **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/django-sports-registration.git]
    cd Sports_project_folder
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv my_venv
    source my_venv/bin/activate  # On Windows use `my_venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

### User Registration
- Users can register through the registration page at `/register/`.
- Upon registration, users can select their account type (Admin or Basic).

### Logging In and Out
- Users can log in at `/login/` and log out at `/logout/`.

### Registering for Sports
- After logging in, users can register for a sport by filling out the registration form.

### Viewing Registrants
- Logged-in users can view a list of registered teams.

### Admin Features
- Admins can delete registrations.

### Contact
Dimpal -https://github.com/Dimplektech

