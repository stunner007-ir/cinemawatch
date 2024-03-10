# CinemaWatch - Django REST API Backend Project

CinemaWatch is a Django REST API backend project designed to serve as a clone of IMDb, focusing on movie and TV show information. This README provides an overview of the project structure, setup instructions, and usage guidelines.

# Prerequisites

- Python 3.7 or higher
- Django 3.2 or higher
- Postman (For API Testing)
- Django REST Framework 3.12 or higher
- pip (Python package manager)

## Features

- CRUD operations for managing movies and TV shows
- User authentication and authorization
- Search functionality for finding movies and TV shows
- Rating and reviewing system

## Project Structure

- `cinemawatch/`: The root directory of the project.
- `cinemawatch/settings.py`: Configuration settings for the Django project.
- `users_app/`: Manages user authentication and authorization.
- `watchlist_app/`: Manages Watchlists and Reviews.
- `requirements.txt`: List of Python dependencies required for the project.
- `manage.py`: Django's command-line utility for administrative tasks.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/stunner007-ir/cinemawatch.git
   cd cinemawatch

   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate

   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:

   ```bash
   python manage.py runserver

   ```

6. Access the API at http://localhost:8000/

## API Endpoints

### Authentication

- `POST /login/`: Log in to the system and obtain an authentication token.
- `POST /register/`: Register a new user.
- `POST /logout/`: Log out from the system.

### Movies

- `GET /list/`: Retrieve a list of all movies.
- `GET /<int:pk>/`: Retrieve details of a specific movie by its ID.
- `GET /list2/`: Retrieve a list of all watchlists.

### Reviews

- `POST /<int:pk>/review-create/`: Create a new review for a specific movie.
- `GET /<int:pk>/reviews/`: Retrieve all reviews for a specific movie.
- `GET /review/<int:pk>/`: Retrieve details of a specific review.
- `GET /reviews/`: Retrieve all reviews published by a particular user.

### Additional Functionality

- `admin/`: Django admin interface for administrative tasks.
- `watch/`: Include additional APIs related to the watchlist app.
- `account/`: Include additional APIs related to the user app.

### Contributors

- Backend - [Ishu Raj](https://github.com/stunner007-ir)
<!-- - [Contributor Name](https://github.com/contributor-username) -->

### License

This project is licensed under the [MIT License](LICENSE). 
