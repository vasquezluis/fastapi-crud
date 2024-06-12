from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = ''

# create_engine is a function that returns a new Engine instance
engine = create_engine(URL_DATABASE)

# sessionmaker is a factory function that creates a new Session class with the given parameters
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base is a factory function that constructs a base class for declarative class definitions
Base = declarative_base()