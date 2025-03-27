from sqlalchemy import Column, DateTime, Integer, String, func
from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(40), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)