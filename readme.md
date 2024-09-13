# Django CRUD Application with AJAX and Authentication

This is a Django-based web application that allows users to perform CRUD (Create, Read, Update, Delete) operations on student records. The application also features AJAX for seamless data manipulation and authentication modules for secure access.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)


## Features
- Create, Read, Update, and Delete (CRUD) operations on student records
- AJAX integration for real-time updates without page reload
- User authentication with registration, login, and logout
- Secure access with session management

## Technologies Used
- **Django**: Backend framework
- **SQLite**: Default database used
- **AJAX**: Asynchronous data fetching and updating
- **HTML/CSS/JavaScript**: Frontend technologies

## Installation

- Follow these steps to set up the project locally:

### Prerequisites
- Python 3.10.11 installed
- pip (Python package installer)


### Steps
   
1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate.bat

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Apply migrations and create superuser:**
    ```bash
   python manage.py migrate
   python manage.py createsuperuser

4. **Run the server:**
    ```bash   
    python manage.py runserver

## Usage
- Access the application at http://localhost:8000
- Manage student records with CRUD operations at /students/.