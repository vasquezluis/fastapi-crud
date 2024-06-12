from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class User(Base):
    # instance of the table
    __tablename__ = "users"

    # index is for the database to index the column
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)

class Post(Base):
    # instance of the table
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(String(100), index=True)
    published = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))