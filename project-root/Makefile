# Load .env variables
include .env
export $(shell sed 's/=.*//' .env)

# Commands for All Containers
start:
	@echo "Starting all Docker containers (backend and frontend)..."
	$(DOCKER_COMPOSE) up --build -d

stop:
	@echo "Stopping all Docker containers (backend and frontend)..."
	$(DOCKER_COMPOSE) down

restart:
	@echo "Restarting all Docker containers (backend and frontend)..."
	$(DOCKER_COMPOSE) down && $(DOCKER_COMPOSE) up --build -d

status:
	@echo "Checking the status of all running containers..."
	docker ps

logs:
	@echo "Displaying logs for all services..."
	$(DOCKER_COMPOSE) logs -f

clean:
	@echo "Cleaning up unused Docker volumes..."
	docker volume prune -f

# Commands for Backend Only
start-backend:
	@echo "Starting only the backend service..."
	$(DOCKER_COMPOSE) up --build -d $(BACKEND_SERVICE)

logs-backend:
	@echo "Displaying logs for the backend service..."
	$(DOCKER_COMPOSE) logs -f $(BACKEND_SERVICE)

exec-backend:
	@echo "Entering the backend container..."
	docker exec -it $(BACKEND_SERVICE) /bin/bash

test-backend:
	@echo "Running tests in the backend container..."
	docker exec -it $(BACKEND_SERVICE) pytest

# Commands for Frontend Only
start-frontend:
	@echo "Starting only the frontend service..."
	$(DOCKER_COMPOSE) up --build -d $(FRONTEND_SERVICE)

logs-frontend:
	@echo "Displaying logs for the frontend service..."
	$(DOCKER_COMPOSE) logs -f $(FRONTEND_SERVICE)

exec-frontend:
	@echo "Entering the frontend container..."
	docker exec -it $(FRONTEND_SERVICE) /bin/bash

# Access PostgreSQL
psql:
	@echo "Accessing PostgreSQL database..."
	docker exec -it $(POSTGRES_SERVICE) psql -U your_postgres_user -d your_postgres_db
	
logs-postgres:
	@echo "Displaying logs for the PostgreSQL service..."
	docker logs -f $(POSTGRES_SERVICE)

# Environment Switching Commands
toprod:
	@echo "Switching to production environment for all services..."
	@sed -i '' 's/^ENV=dev/ENV=prod/' $(ENV_FILE) || sed -i 's/^ENV=dev/ENV=prod/' $(ENV_FILE)
	$(DOCKER_COMPOSE) down && $(DOCKER_COMPOSE) up --build -d
	@echo "Environment switched to production!"

todev:
	@echo "Switching to development environment for all services..."
	@sed -i '' 's/^ENV=prod/ENV=dev/' $(ENV_FILE) || sed -i 's/^ENV=prod/ENV=dev/' $(ENV_FILE)
	$(DOCKER_COMPOSE) down && $(DOCKER_COMPOSE) up --build -d
	@echo "Environment switched to development!"
