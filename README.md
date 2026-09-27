# Vehicle Service Booking System

A Flask-based web application for booking vehicle servicing online. Users can enter their vehicle and contact details, select a service type and preferred date, and create a service booking.

## Features

- Vehicle service booking form
- Customer and vehicle details
- Vehicle type selection
- Service type selection
- Preferred service date
- 10-digit contact number validation
- Display of submitted bookings
- JSON API for bookings
- Health check endpoint
- Automated testing with pytest
- Code linting with flake8
- Docker containerization
- GitHub Actions CI/CD
- Render deployment

## Technologies Used

- Python
- Flask
- pytest
- flake8
- Gunicorn
- Docker
- GitHub Actions
- Render
- GitHub

## Project Structure

```text
Vehicle-Service-Booking/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── templates/
│   └── index.html
├── .dockerignore
├── .gitignore
├── Dockerfile
├── app.py
├── requirements.txt
├── test_app.py
└── README.md