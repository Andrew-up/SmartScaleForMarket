import os
import sqlite3

name_database = "test"
pathDB = os.path.dirname(__file__) + '\\..\\data_base/db.db'


class TableProduct:
    id_product = "id_product"
    name_product = "name_product"


createTableQuery = f"""
        CREATE TABLE IF NOT EXISTS {name_database}(
        {TableProduct.id_product} integer NOT NULL PRIMARY KEY,
        {TableProduct.name_product} text
        )
"""

# def findItemByName(productName):
#     if testConnect() == 0:
#         db = sqlite3.connect(pathDB)
#         cursor = db.cursor()
#         selectRequestText = f"""SELECT * FROM {name_database} db where db.id_product==productName"""
#         cursor.execute(selectRequestText)
#         record = cursor.fetchall()
#         cursor.close()
#         db.close()
#         return record

def findAllByTest():
    if testConnect() == 0:
        db = sqlite3.connect(pathDB)
        cursor = db.cursor()
        selectRequestText = f"""SELECT * FROM {name_database}"""
        cursor.execute(selectRequestText)
        record = cursor.fetchall()
        cursor.close()
        db.close()
        return record
    else:
        print("что то пошло не так при получении")


def insertRequest(product_name):
    if testConnect() == 0:
        db = sqlite3.connect(pathDB)
        cursor = db.cursor()
        insert_request_text = f""" INSERT INTO {name_database}({TableProduct.name_product}) VALUES (\"{product_name}\")"""
        cursor.execute(insert_request_text)
        db.commit()
        cursor.close()
        db.close()
        return cursor.lastrowid
    else:
        print("что то пошло не так при добавлении")


def testConnect():
    global db
    print(pathDB)
    status_connect = 0
    try:
        db = sqlite3.connect(pathDB)
        cursor = db.cursor()
        # cursor.execute("skjgsdjsdbfdsf")
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name= \"{name_database}\"")
        if not cursor.fetchall():
            cursor.execute(createTableQuery)
            print(f"База данных \"{name_database}\" создана и успешно подключена к SQLite")
        else:
            print(f"База данных \"{name_database}\" успешно подключена к SQLite")
        cursor.close()
    except sqlite3.Error as error:
        status_connect = 1
        print("Ошибка при подключении к sqlite : ", error)
    finally:
        if (db):
            db.close()
            print("Соединение с SQLite закрыто")

    return status_connect


if __name__ == '__main__':
    name_product = 'Помидор'
    print("добавлена новая запись, id: " + str(insertRequest(name_product)))
    print(findAllByTest())
    # testConnect()
