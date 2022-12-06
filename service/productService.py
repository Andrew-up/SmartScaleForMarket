# from repository.productRepository import ProductRepository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from repository.productRepository import ProductRepository

engine = create_engine("sqlite:///../data_base/db.db", echo=True)

if __name__ == '__main__':
    # ps = ProductRepository()

    ps = ProductRepository()
    sss = ps.find_all()
    # print(sss[1].name_Product)
    print("test")
    pass



