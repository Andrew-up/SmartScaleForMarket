import backend.service.productService


class Product(object):

    def __init__(self, name_Product=None):
        self.id_Product = 0
        self.name_Product = name_Product

    def get_all_product(self) -> list["Product"]:
        return backend.service.productService.findAll()

    def add_product(self):
        new_product = backend.service.productService.addProduct(self.name_Product)
        return new_product

    def clear_base(self):
        result = backend.service.productService.deleteAll()
        return result



