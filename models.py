from sqlalchemy import String, Integer, Column, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Links(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True)
    url = Column(String, primary_key=False, nullable=False)
    short = Column(String, primary_key=False, nullable=False)
    expired = Column(Date, primary_key=False, nullable=False)
