import sqlite3


def check_connection():
    try:
        db = sqlite3.connect('sila.db')
        db_cursor = db.cursor()
        return db, db_cursor
    except Exception as e:
        print(f'Ошибка: {e}')
        return None, None
