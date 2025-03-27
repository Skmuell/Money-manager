from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(
    settings.DB_URI,
    pool_size=settings.DB_ENGINE_POOL_SIZE,
    max_overflow=settings.DB_ENGINE_MAX_OVERFLOW,
    pool_pre_ping=settings.DB_POOL_PRE_PING,
)

SessionLocal = sessionmaker(bind=engine)


@contextmanager
def get_session():
    """Context manager to ensure the session is closed after use."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

# if __name__ == "__main__":
#     from sqlalchemy import text

#     with get_session() as session:
#         print("## Testing database connection...")
#         result = session.execute(text("SELECT 1"))

#         if result.scalar() == 1:
#             print("## Connection test successful!")
#         else:
#             print("## Connection test failed.")