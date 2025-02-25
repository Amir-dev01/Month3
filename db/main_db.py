import sqlite3
from db import queries


db = sqlite3.connect('db/store.sqlite3', check_same_thread=False)
cursor = db.cursor()


async def create_tables():
    try:
        cursor.execute(queries.CREATE_TABLE_store)
        cursor.execute(queries.CREATE_TABLE_store_details)
        cursor.execute(queries.CREATE_TABLE_collection)
        db.commit()
        print("Таблицы созданы успешно!")
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")


async def sql_insert_store(name_product, price, size, product_id, photo):
    try:
        cursor.execute(queries.INSERT_store_query, (name_product, price, size, product_id, photo))
        db.commit()
    except Exception as e:
        print(f"Ошибка при добавлении товара: {e}")


async def sql_insert_store_details(category, product_id):
    try:
        cursor.execute(queries.INSERT_store_details_query, (category, product_id))
        db.commit()
    except Exception as e:
        print(f"Ошибка при добавлении деталей товара: {e}")


async def sql_insert_collection_query(product_id, collection):
    try:
        cursor.execute(queries.INSERT_collection_query, (product_id, collection))
        db.commit()
    except Exception as e:
        print(f"Ошибка при добавлении коллекции: {e}")


def fetch_all_products():
    try:
        conn = sqlite3.connect('db/store.sqlite3')
        conn.row_factory = sqlite3.Row
        products = conn.execute(queries.FETCH_ALL_PRODUCTS_QUERY).fetchall()
        conn.close()
        return products
    except Exception as e:
        print(f"Ошибка при получении товаров: {e}")
        return []