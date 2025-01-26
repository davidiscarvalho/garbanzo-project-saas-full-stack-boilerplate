# Makefile instructions

## All Services Commands:
start: Builds and starts both backend and frontend containers.
stop: Stops and removes all containers.
restart: Restarts all containers with fresh builds.
logs: Shows logs for all services (backend and frontend).

## Service-Specific Commands:
- Backend:
start-backend
logs-backend
exec-backend
test-backend

- Frontend:
start-frontend
logs-frontend
exec-frontend

### Environment Switching:
toprod and todev apply to both containers and restart them to reflect the changes in the .env file.

## Global Commands (All Services):
- Start all services:
make start

- Stop all services:
make stop

- Restart all services:
make restart

- Check status of containers:
make status

- View logs for all services:
make logs

- Switch to production:
make toprod

- Switch to development:
make todev

- Backend-Specific Commands:
- Start only the backend:
make start-backend

- View backend logs:
make logs-backend

- Enter the backend container:
make exec-backend

- Run backend tests:
make test-backend

- Frontend-Specific Commands:
- Start only the frontend:
make start-frontend

- View frontend logs:
make logs-frontend

- Enter the frontend container:
make exec-frontend

- Postgres-Specific Commands:
- Access the PostgreSQL container's shell:
make psql

- logs-postgres: Displays the logs for the PostgreSQL container.
make logs-postgres

## Assumptions
- The .env file has all the variables.