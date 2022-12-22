# from repository.productRepository import ProductRepository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.repository import productRepository
from backend.model.product import Product
from definitions import DATABASE_DIR

# from repository.productRepository import ProductRepository
engine = create_engine(f"sqlite:///{DATABASE_DIR}")
get_session = sessionmaker(bind=engine)


def getById(idProduct):
    session = get_session()
    repo = productRepository.ProductRepository(session)
    item = repo.get_by_id(id_product=idProduct)
    session.close()
    return item


def getProductByLabel(labelsProduct: str):
    session = get_session()
    repo = productRepository.ProductRepository(session)
    item = repo.get_by_label(label_product=labelsProduct)
    session.close()
    return item


def addProductByName(product_name: str):
    session = get_session()
    repo = productRepository.ProductRepository(session)
    new_prod = Product(name_Product=product_name)
    new_item = repo.add(new_prod)
    session.close()
    return new_item


def addProduct(product: Product):
    session = get_session()
    repo = productRepository.ProductRepository(session)
    new_prod = repo.add(product)
    session.close()
    return new_prod


def addProducts(products: list[Product]):
    session = get_session()
    repo = productRepository.ProductRepository(session)
    new_products = repo.add_list_product(products)
    session.close()
    return new_products


def findAll() -> list[Product]:
    session = get_session()
    repo = productRepository.ProductRepository(session)
    all_prod = repo.find_all()
    session.close()
    return all_prod


def find_products_by_name(find_string: str) -> list[Product]:
    session = get_session()
    repo = productRepository.ProductRepository(session)
    all_prod = repo.find_by_name(find_string)
    session.close()
    return all_prod


def findAllCategories():
    session = get_session()
    repo = productRepository.ProductRepository(session)
    cat = {}
    all_prod = repo.find_all()
    for a in all_prod:
        cat[a.categorical_id] = a.categorical_name
    session.close()
    return cat


def deleteAll():
    session = get_session()
    repo = productRepository.ProductRepository(session)
    all_delete = repo.delete_all()
    session.close()
    return all_delete


def editProductById(id_Product: int, new_product: Product):
    session = get_session()
    repo = productRepository.ProductRepository(session)
    product = repo.get_by_id(id_Product)
    edit = repo.edit_product(product, new_product)
    session.close()
    return edit


if __name__ == '__main__':
    #     print(getById(1).id_Product)
    #     print(addProduct("Пример 1"))
    find_products_by_name('б')
    # print(deleteAll())
    pass
