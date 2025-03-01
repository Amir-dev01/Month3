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

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    try:
        conn = get_db_connection()
        products = conn.execute(queries.FETCH_ALL_PRODUCTS_QUERY).fetchall()
        conn.close()
        return products
    except Exception as e:
        print(f"Ошибка при получении товаров: {e}")
        return []

def update_product_field(product_id, field_name, new_value):
    conn = get_db_connection()

    store_table = ['name_product', 'price', 'size', 'product_id', 'photo']
    store_details_table = ['category', 'product_id']
    collection_products_table = ['collection', 'product_id']

    try:
        if field_name in store_table:
            query = f'UPDATE store SET {field_name} = ? WHERE product_id = ?'
        elif field_name in store_details_table:
            query = f'UPDATE store_details SET {field_name} = ? WHERE product_id = ?'
        elif field_name in collection_products_table:
            query = f'UPDATE collection_products SET {field_name} = ? WHERE product_id = ?'

        else:
            raise ValueError(f'Нет такого поля как {field_name}')

        conn.execute(query, (new_value, product_id))
        conn.commit()

    except sqlite3.OperationalError as error:
        print(f'Ошибка - {error}')

    finally:
        conn.close()
