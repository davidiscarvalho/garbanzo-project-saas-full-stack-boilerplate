# ./main.py

from fastapi import FastAPI, Request
from sqlmodel import SQLModel, create_engine, Session
import uvicorn

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from core.config import settings # Import settings from the core config module
# Import routers
from routers.limiter import limiter


# Initialize app
app = FastAPI()

# Database setup
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)

# Database session (Dependency)
def get_session():
    with Session(engine) as session:
        yield session


# Routers
#app.include_router(user_router)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Health check endpoint
@app.get("/")
@limiter.limit("10/minute")
def check_server_run(
    request: Request
):
    return "Server is running."




# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)