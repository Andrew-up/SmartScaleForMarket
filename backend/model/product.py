from sqlalchemy import Column, ForeignKey, Integer, String, Identity, BLOB, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from definitions import DATABASE_DIR

Base = declarative_base()
from migrate.changeset import *


# from mi


class Product(Base):
    __tablename__ = 'Product'
    id_Product = Column(Integer, primary_key=True)
    name_Product = Column(String(250), nullable=False)
    image_Product = Column(BLOB)


engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


def add_column():
    db_meta = MetaData(bind=engine)
    table = Table('Product', db_meta)
    image_Product = Column('image_product', BLOB)
    create_column(image_Product, table)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
