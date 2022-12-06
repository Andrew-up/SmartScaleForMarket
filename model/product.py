from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../data_base/db.db", echo=True)

Base = declarative_base()


class Product(Base):
    __tablename__ = 'Product'

    id_Product = Column(Integer, primary_key=True)
    name_Product = Column(String(250), nullable=False)


Base.metadata.create_all(engine)
