# Task Management App

A simple Django web app for managing daily tasks with progress tracking and user authentication.

## Features
- User registration, login, and logout
- Change password, update email, delete account
- User profile with optional profile picture (and default image if none)
- Add, edit, and delete tasks
- Mark tasks as complete
- Search for tasks by title
- Prioritize tasks (High / Medium / Low)
- Task creation and completion dates
- Responsive design with custom templates

  
## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/mikeydows/Task-Management-App.git
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Technologies Used
- Django
- HTML, CSS, JavaScript
- SQLite
- Django built-in auth system
- Django’s MEDIA_ROOT and MEDIA_URL
