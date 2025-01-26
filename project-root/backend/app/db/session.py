# ./db/session.py

from sqlmodel import SQLModel, create_engine, Session

from core.config import settings # Import settings from the core config module

# Database setup
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)

# Database session (Dependency)
def get_session():
    with Session(engine) as session:
        yield session
