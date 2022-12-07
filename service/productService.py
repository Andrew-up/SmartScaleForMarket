# from repository.productRepository import ProductRepository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from repository import productRepository
from model.product import Product, Base
from definitions import DATABASE_DIR
# from repository.productRepository import ProductRepository
engine = create_engine(f"sqlite:///{DATABASE_DIR}")
get_session = sessionmaker(bind=engine)


def getById(idProduct):
    session = get_session()
    repo = productRepository.ProductRepository(session)
    item = repo.get(idProduct)
    session.close()
    return item


def addProduct(item_name: str):
    session = get_session()
    repo = productRepository.ProductRepository(session)
    new_prod = Product(name_Product=item_name)
    new_item = repo.add(new_prod)
    session.close()
    return new_item


def findAll():
    session = get_session()
    repo = productRepository.ProductRepository(session)
    all_prod = repo.find_all()
    session.close()
    return all_prod


def deleteAll():
    session = get_session()
    repo = productRepository.ProductRepository(session)
    all_delete = repo.delete_all()
    session.close()
    return all_delete


if __name__ == '__main__':
    #     print(getById(1).id_Product)
    #     print(addProduct("Пример 1"))
    print(findAll())
    # print(deleteAll())
    pass
