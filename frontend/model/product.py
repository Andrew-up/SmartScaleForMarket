import backend.service.productService


class Product(object):

    def __init__(self, name_Product=None):
        self.id_Product = 0
        self.name_Product = name_Product
        self.image_Product = 0
        self.categorical_name = ''
        self.categorical_id = ''

    def get_all_product(self) -> list["Product"]:
        return backend.service.productService.findAll()

    def get_products_by_name(self, name_product: str) -> list["Product"]:
        return backend.service.productService.find_products_by_name(name_product)

    def add_product(self):
        new_product = backend.service.productService.addProductByName(self.name_Product)
        return new_product

    def clear_base(self):
        result = backend.service.productService.deleteAll()
        return result

    def edit_product_by_id(self, id_product: int, new_Product: "Product"):
        edit = backend.service.productService.editProductById(id_product, new_Product)
        return edit

    def get_product_by_id(self, id_product: int):
        res = backend.service.productService.getById(idProduct=id_product)
        return res

    def get_product_by_label(self, product_labels: str):
        res = backend.service.productService.getProductByLabel(labelsProduct=product_labels)
        return res
