# Library API

A modular REST API built with Python and Flask for managing a library. This project includes separate services for user registration, book management, and book borrowing functionalities. The project is structured using a microservices architecture, allowing each service to operate independently and communicate with others as needed.

## Features

- **User Registration**: Manage user accounts.
- **Book Management**: Add, update, and retrieve books in the library.
- **Book Borrowing**: Track which books are borrowed by users, with return functionality.
- **Microservices Architecture**: Each feature is managed by an independent service, improving scalability and modularity.

## Technologies Used

- **Python**
- **Flask** and **Flask-SQLAlchemy**
- **PostgreSQL** for database management
- **Docker** and **Docker Compose** for containerized services

## Project Structure

The project is divided into three main services, each with its own codebase, dependencies, and database setup:

- **User Service**: Manages user registration and information, running on port 5001.
- **Book Service**: Manages book catalog information, running on port 5002.
- **Borrowing Service**: Tracks borrowing transactions, running on port 5003.

## Installation and Setup

### Prerequisites

Ensure **Docker** and **Docker Compose** are installed on your system.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/library-api.git
   cd library-api

2. **Start the Services with Docker Compose**: Run the following command to build and start all services:
   ```bash
   docker-compose up --build

3. **Access the API**:
   - User Service: http://localhost:5001
   - Book Service: http://localhost:5002
   - Borrowing Service: http://localhost:5003

4. **Stop the Services:**: To stop all services, press Ctrl+C or run:
   ```bash
   docker-compose down

## Future Improvements

- **Enhanced Inter-Service Communication**: Implement more secure and efficient methods for service-to-service communication.
- **Authentication and Authorization**: Add user authentication (e.g., JWT).
- **Testing**: Include unit tests and integration tests for each service.

## Access Endpoints

Each service includes endpoints for specific functionalities. Refer to individual service documentation for detailed routes.
