from sqlalchemy import Column, ForeignKey, Integer, String, Identity, BLOB, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from definitions import DATABASE_DIR

Base = declarative_base()
from migrate.changeset import *


class Product(Base):
    __tablename__ = 'Product'
    id_Product = Column(Integer, primary_key=True)
    name_Product = Column(String(250))
    image_Product = Column(BLOB)
    categorical_name = Column(String(250), unique=True)
    categorical_id = Column(Integer, unique=True)

    def set_name_Product(self, name_Product: str):
        self.name_Product = name_Product

    def set_categorical_name(self, categorical_name: str):
        self.categorical_name = categorical_name

    def set_categorical_id(self, categorical_id: int):
        self.categorical_id = categorical_id



engine = create_engine(f"sqlite:///{DATABASE_DIR}", echo=True)


def add_column(name_column: str, tableName: str):
    db_meta = MetaData(bind=engine)
    table = Table(tableName, db_meta)
    name_column = Column(name_column, String(250))
    create_column(name_column, table)


if __name__ == '__main__':
    # add_column("categorical_name", "Product")
    Base.metadata.create_all(engine)
