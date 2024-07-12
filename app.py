from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these values with your Redshift cluster details
host = 'your-redshift-cluster-endpoint'
port = '5439'
dbname = 'your-database-name'
user = 'your-username'
password = 'your-password'

# Create an engine
engine = create_engine(f'postgresql://admin:cWR0RwyL715nufQabXHme5ou8QASIxvh@dpg-cq7vl3ggph6c73ev22bg-a.oregon-postgres.render.com/demodb_gp75')


# Define a base class
Base = declarative_base()

# Define your table as a class
class YourTableName(Base):
    __tablename__ = 'friends'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create the table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert records
try:
    records = [
        YourTableName(id=1, name='Alice', age=30),
        YourTableName(id=2, name='Bob', age=25),
        YourTableName(id=3, name='Charlie', age=35)
    ]
    session.add_all(records)
    session.commit()
    print("Records inserted successfully")
except Exception as e:
    print(f"Error inserting records: {e}")
    session.rollback()
finally:
    session.close()
