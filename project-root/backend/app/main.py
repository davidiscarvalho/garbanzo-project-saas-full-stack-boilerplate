# ./main.py

from fastapi import FastAPI, Request
import uvicorn

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

# Import routers
from routers.limiter import limiter
from routers import core, userAccount, user


# Initialize app
app = FastAPI()

# Routers
app.include_router(core.router)
app.include_router(userAccount.router)
app.include_router(user.router)

# Add rate limiter to app
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