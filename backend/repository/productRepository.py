from backend.model.product import Product
from backend.repository.abstractRepository import AbstractRepository


class ProductRepository(AbstractRepository):

    def get(self, id_item) -> Product:
        return self.session.query(Product).first()

    def add(self, data: Product) -> Product.id_Product:
        self.session.add(data)
        self.session.commit()
        # self.session.flush()
        return data.id_Product

    def find_all(self) -> list[Product]:
        return self.session.query(Product).all()

    def delete_all(self) -> str:
        self.session.query(Product).delete()
        self.session.commit()
        return "База очищена"

    def __init__(self, session):
        self.session = session
