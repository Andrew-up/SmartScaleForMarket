from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.product import Product

engine = create_engine("sqlite:///../data_base/db.db", echo=True)


class ProductRepository:

    def find_all(self) -> list[Product]:
        sessions = sessionmaker(bind=engine)
        s = sessions()
        return s.session.query(Product).all()

    # def __init__(self, session):
    #     self.session = session

    pass

    # def find_product_by_id(self, id_product: int) -> Product:
    #     return self.session.query(Product)
