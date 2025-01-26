1. Project Setup
- [x] Create the project directory structure with backend/, frontend/, and root files.
- [x] Initialize Git repository for version control.
- [x] Create .gitignore files in both backend and frontend folders.
- [x] Create a README.md file for project documentation.

2. Backend (FastAPI) Setup
- [x] Set up FastAPI app in backend/app/.
- [x] Create main.py with basic FastAPI app.
- [ ] Set up routing in app/routers/.
- [ ] Create models in app/models/.
- [ ] Implement services in app/services/.
- [ ] Add tests in app/tests/.
- [x] Configure environment variables for backend in .env:
- [ ] Add DATABASE_URL, SECRET_KEY, and other necessary vars.
- [ ] Set up database (Postgres) for local development:
- [ ] Configure DATABASE_URL in .env for local (sqlite for dev and Postgres for prod).
- [ ] Add Alembic for database migrations.
- [ ] Install necessary Python dependencies:
- [x] pip install fastapi uvicorn sqlalchemy psycopg2 alembic
- [ ] Create Dockerfile for backend container:
- [x] Set up Python environment.
- [ ] Install dependencies from requirements.txt.
- [ ] Expose necessary ports (8000).
- [x] Run the FastAPI app with Uvicorn.
3. Frontend (React) Setup
- [ ] Create React app in frontend/.
- [ ] Set up components in frontend/src/components/.
- [ ] Set up pages in frontend/src/pages/.
- [ ] Add basic styling in frontend/src/styles/.
- [ ] Configure environment variables for frontend in .env:
- [ ] Set REACT_APP_API_URL to point to the backend API.
- [ ] Install necessary npm packages:
- [ ] npm install react-router-dom axios
- [ ] Create Dockerfile for frontend container:
- [ ] Build React app using Node.js.
- [ ] Use Nginx to serve the static files from /build.
4. Docker and Docker Compose Setup
- [ ] Create docker-compose.yml to link backend, frontend, and Postgres:
- [ ] Set up services for backend, frontend, and postgres.
- [ ] Add environment variable loading with env_file.
- [ ] Define volume mapping for backend and frontend code.
- [ ] Configure Postgres service:
- [ ] Set up environment variables like POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB.
- [ ] Expose Postgres port 5432.
- [ ] Test Docker Compose configuration:
- [ ] Run docker-compose up --build to ensure everything builds and starts.
5. Environment Variables Setup
- [ ] Create .env file for the root of the project:
- [ ] Add ENV, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, etc.
- [ ] Create .env files for both frontend and backend:
- [ ] frontend/.env for React-related environment variables.
- [ ] backend/.env for backend-specific variables (like DATABASE_URL).
6. Development and Testing
- [ ] Develop basic API endpoints in FastAPI (e.g., /users, /subscriptions).
- [ ] Create simple frontend pages to interact with backend API:
- [ ] Create landing page.
- [ ] Create login page.
- [ ] Create homepage.
- [ ] Create user details page.
- [ ] Test backend functionality using Postman or similar tools:
- [ ] Test API routes for CRUD operations.
- [ ] Test database connection (local and production).
- [ ] Test frontend functionality by checking if React can interact with FastAPI.
7. Deployment and Optimization
- [ ] Optimize backend Dockerfile:
- [ ] Minimize image size by removing unnecessary dependencies.
- [ ] Set up for production by removing --reload in Uvicorn.
- [ ] Optimize frontend Dockerfile:
- [ ] Remove unnecessary dev dependencies.
- [ ] Minimize the image size using multi-stage builds.
- [ ] Set up environment for production:
- [ ] Update .env for production settings.
- [ ] Ensure sensitive data is stored securely (e.g., secrets management).
8. Makefile Setup for Automation
- [ ] Create Makefile in the project root:
- [ ] Add commands for build, up, down, logs, etc.
- [ ] Add command for switching environments: todev and toprod.
- [ ] Add command for building and starting both containers: start.
9. Version Control
- [ ] Commit initial project files (GitHub repo).
- [ ] Push code to GitHub after major changes.
10. Documentation
- [ ] Complete README.md:
- [ ] Project overview.
- [ ] Instructions for setting up, running, and testing the app.
- [ ] Docker and environment setup.
- [ ] Document environment variables and their usage.
- [ ] Write API documentation (Postman, Swagger UI, etc.).