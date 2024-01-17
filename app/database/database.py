from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL
# Creating the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# Creating the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()