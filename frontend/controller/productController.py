from frontend.model.product import Product

items = list()


class ProductController(object):

    def __init__(self, model: Product(), view):
        self.model = model
        self.view = view

    def all_products(self) -> list[Product]:
        return self.model.get_all_product()

    def new_product(self, nameProduct: str):
        return self.model.add_product(Product(name_Product=nameProduct))

    def clear_all_data_base(self):
        return self.model.clear_base()


if __name__ == '__main__':
    pass

