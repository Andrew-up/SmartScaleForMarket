from backend.model.product import Product
from backend.repository.abstractRepository import AbstractRepository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, not_


class ProductRepository(AbstractRepository):

    def get(self, id_item) -> Product:
        return self.session.query(Product).get(id)
    def get_last(self) -> Product:
        return self.session.query(Product).order_by(Product.categorical_id.desc()).first()

    def add(self, data: Product) -> Product.id_Product:
        self.session.add(data)
        self.session.commit()
        # self.session.flush()
        return data.id_Product

    def add_list_product(self, data: list[Product]):
        successful_append = list()
        for a in data:
            self.session.add(a)
            self.session.commit()
            successful_append.append(a.id_Product)
        return "успешно добавлены: " + str(successful_append)

    def find_all(self) -> list[Product]:
        return self.session.query(Product).filter(not_(Product.categorical_name.contains('background'))).all()

    def find_all_and_background(self) -> list[Product]:
        return self.session.query(Product).all()

    def find_by_name(self, find_string: str):
        req: list[Product] = self.session.query(Product).filter(not_(Product.categorical_name.contains('background'))).all()
        res = list()
        for a in req:
            # print(a)
            if a.name_Product.lower().find(find_string.lower()) != -1:
                # print(a.name_Product)
                res.append(a)
        return res

    def find_all_categories(self) -> list[Product.categorical_name]:
        return self.session.query(Product.categorical_name).filter(not_(Product.categorical_name.contains('background'))).all()

    def delete_all(self) -> str:
        self.session.query(Product).delete()
        self.session.commit()
        return "База очищена"

    def edit_product(self, product: Product, new_Product: Product):
        x: Product = self.session.query(Product).get(product.id_Product)
        print(product.name_Product)
        x.name_Product = new_Product.name_Product
        x.image_Product = new_Product.image_Product
        self.session.commit()
        return "Обновлено"

    def get_by_id(self, id_product: int):
        return self.session.query(Product).get(id_product)

    def get_by_label(self, label_product: str):
        return self.session.query(Product).filter(Product.categorical_name == label_product).first()

    def __init__(self, session: sessionmaker()):
        self.session = session
