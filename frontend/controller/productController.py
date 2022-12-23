from frontend.model.product import Product

items = list()


class ProductController(object):

    def __init__(self, model: Product(), view):
        self.model = model
        self.view = view

    def all_products(self) -> list[Product]:
        return self.model.get_all_product()

    def find_products_by_name(self, name_product: str) -> list[Product]:
        return self.model.get_products_by_name(name_product)

    def new_product(self, nameProduct: str):
        return self.model.add_product(Product(name_Product=nameProduct))

    def clear_all_data_base(self):
        return self.model.clear_base()

    def edit_product(self, id_product: int, new_Product: Product):
        return self.model.edit_product_by_id(id_product=id_product, new_Product=new_Product)

    def get_Product_by_id(self, id_product: int):
        return self.model.get_product_by_id(id_product)

    def get_product_by_label(self, label_product: str) -> Product:
        return self.model.get_product_by_label(label_product)


if __name__ == '__main__':
    p = ProductController(Product(), ProductController)
    res = p.find_products_by_name("Я")
    print(res)
    pass

