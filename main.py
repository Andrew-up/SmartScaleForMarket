# import UI.main
from model.product import Product
from repository.productRepository import ProductRepository
if __name__ == '__main__':
    prod = ProductRepository()
    print(prod.findAll())
    # UI.main.startApp()
    # model = Product(10, 20)
    # print(model.idProduct)

