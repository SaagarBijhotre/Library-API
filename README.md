# Library API

A simple REST API built with Python and Flask for managing a library. This project includes basic user registration, book management, and book borrowing functionalities. The current structure is monolithic, but future updates will refactor it into a microservices architecture.

## Features

- **User Registration**: Register new users.
- **Book Management**:
  - Add new books.
  - Retrieve a list of books.
- **Book Borrowing**: Mark books as borrowed by users.
- **Welcome Endpoint**: A simple home route to confirm that the server is running.

## Technologies Used

- **Python**
- **Flask** and **Flask-SQLAlchemy**
- **SQLite** for database management

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/library-api.git
   cd library-api

2. **Create a virtual environment**:
   ```bash
   python -m venv venv

3. **Activate the virtual environment**:
   ```bash
   .\venv\Scripts\Activate

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt

5. ***Run the application**:
   ```bash
   python app.py

6. **Access the API**:
   - The API will be available at http://127.0.0.1:5000/
