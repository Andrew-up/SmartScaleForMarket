from repository.productRepository import ProductRepository


def get_all_product():
    repository = ProductRepository()
    repository.findAll()
    pass