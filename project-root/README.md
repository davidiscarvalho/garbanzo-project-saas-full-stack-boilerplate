# Project Name: Multi-Service App with FastAPI, React, Postgres, and Docker

## Overview
This project provides a boilerplate setup for a full-stack application with:
- Backend: FastAPI (Python) serving APIs.
- Frontend: React (JavaScript) for the user interface.
- Database: PostgreSQL for persistent data storage.
- Containerization: Docker to run both frontend and backend services in isolated containers.
- Docker Compose: Used to orchestrate multi-container setup for development and production environments.

## Create a .env File

Create a .env file at the root of the project (or copy .env.example if provided). It should contain the following environment variables:
# Global environment variables
ENV=dev
BACKEND_PORT=8000
FRONTEND_PORT=3000
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
DATABASE_URL=postgresql://your_postgres_user:your_postgres_password@postgres:5432/your_postgres_db
REACT_APP_API_URL=http://localhost:8000


### Build and Run the Containers
You can build and run the containers using Docker Compose. This will start all services, including backend, frontend, and PostgreSQL.

- To start all services:
docker-compose up --build

This command will:
Build the Docker images for both the backend and frontend services.
Run the backend on port 8000 (accessible at http://localhost:8000).
Run the frontend on port 3000 (accessible at http://localhost:3000).
Start PostgreSQL on port 5432.

- To start the services in detached mode (background):
docker-compose up -d --build

- Accessing the Application
Once the containers are up and running, you can access:
Frontend (React): Open http://localhost:3000 in your browser.
Backend (FastAPI): Open http://localhost:8000/docs for the interactive API documentation.

### Stopping the Services
- To stop the services, use:
docker-compose down
This will stop and remove the containers but preserve the volume data.

### Development Environment
For development, both the backend and frontend services are set up to live-reload on code changes.
The backend uses uvicorn with the --reload flag for automatic reloading during development.
The frontend uses webpack and react-scripts to automatically rebuild and reload the app.


## Commands
### Switching Between Development and Production Environments
- To switch to production:
make toprod

- To switch to development:
make todev

These commands will automatically update the .env file and adjust the necessary variables for the respective environment.

### Makefile
The Makefile includes helpful commands for managing your services:

- start all services:
make start

- Stop all services:
make stop

- View logs (for backend and frontend):
make logs

Switch to production environment:- 
make toprod

- Switch to development environment:
make todev

## Folder Structure
The project is organized as follows:
project-root/
├── backend/
│   ├── app/           # FastAPI application code
│   ├── .env           # Backend-specific environment variables
│   ├── Dockerfile     # Backend Dockerfile
│   ├── requirements.txt # Python dependencies
├── frontend/
│   ├── src/           # React application source code
│   ├── .env           # Frontend-specific environment variables
│   ├── Dockerfile     # Frontend Dockerfile
│   ├── package.json   # JavaScript dependencies
├── .env               # Global environment variables for both services
├── docker-compose.yml # Multi-container orchestration
├── Makefile           # Automation file for common tasks
└── README.md          # Project documentation

## Troubleshooting
- Port Conflicts: Make sure that the ports 8000 (backend) and 3000 (frontend) are available on your machine. You can modify the port numbers in the .env file if needed.
- Permissions: Ensure that Docker has the required permissions to read from and write to the directories.