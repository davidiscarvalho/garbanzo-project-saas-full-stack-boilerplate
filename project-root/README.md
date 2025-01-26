# Project Name: Multi-Service App with FastAPI, React, Postgres, and Docker

## Overview
This project provides a boilerplate setup for a full-stack application with:
- Backend: FastAPI (Python) serving APIs.
- Frontend: React (JavaScript) for the user interface.
- Database: PostgreSQL in a production environment, and SQLite for development, for persistent data storage.
- Containerization: Docker to run both frontend and backend services in isolated containers.
- Docker Compose: Used to orchestrate multi-container setup for development and production environments.

## Create a .env File

Create a .env file at the root of the project (or copy .env.example if provided). It should contain the following environment variables:
# Global environment variables

## Build and Run the Containers

## Commands
### Switching Between Development and Production Environments
- To switch to production:
make toprod

- To switch to development:
make todev

These commands will automatically update the .env file and adjust the necessary variables for the respective environment.

## Makefile
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