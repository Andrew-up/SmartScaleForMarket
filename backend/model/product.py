from sqlalchemy import Column, ForeignKey, Integer, String, Identity
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from definitions import DATABASE_DIR
Base = declarative_base()


class Product(Base):
    __tablename__ = 'Product'
    id_Product = Column(Integer, primary_key=True)
    name_Product = Column(String(250), nullable=False)


engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

