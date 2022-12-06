from model.product import Product
from service.createDataBase import sendRequestDataBase


class ProductRepository:
    model = Product

    def findAll(self) -> Product:
        return sendRequestDataBase(f"SELECT * FROM test")

    



