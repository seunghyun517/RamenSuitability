from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://{username}:{password}@{host}:{port}/{db_name}".format(
    username='postgres', password='postgres', host='127.0.0.1', port='5432', db_name='foodweather'
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()