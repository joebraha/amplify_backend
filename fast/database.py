from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "postgresql+psycopg2://postgres:data@localhost/Amplify"

# db_url = "postgresql://postgres:16684ccc@localhost/Amplify"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


    
