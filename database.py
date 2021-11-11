from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base=declarative_base()

class Recording(Base):
    __tablename__='All_Recordings'
    id=Column(Integer,primary_key=True)
    path=Column(String)
    
    def __str__(self):
        return self.path

if __name__=='__main__':
    engine=create_engine('sqlite:///project.db',echo=True)
    Base.metadata.create_all(engine)
