import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def check_connection(self):
        try:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()
            return self.connection, self.cursor
        except Exception as e:
            print(f'Ошибка: {e}')
            return None, None

    def get_gs(self, gs_id, table):
        self.connection, self.cursor = self.check_connection()
        if self.connection and self.cursor:
            try:
                result = self.cursor.execute(
                    "SELECT gs_name, gs_description FROM {table_name} WHERE gs_id == '{key}'".format(key=gs_id,
                                                                                                     table_name=table)).fetchone()
                return result
            except sqlite3.Error as e:
                print("Ошибка SQLite:", e)
            finally:
                if self.cursor:
                    self.cursor.close()
                if self.connection:
                    self.connection.close()

    def get_all_gs_tables(self):
        self.connection, self.cursor = self.check_connection()
        if self.connection and self.cursor:
            try:
                result = self.cursor.execute("SELECT gs_id, gs_full_name FROM all_gs_tables").fetchall()
                return result
            except sqlite3.Error as e:
                print("Ошибка SQLite:", e)
            finally:
                if self.cursor:
                    self.cursor.close()
                if self.connection:
                    self.connection.close()

    def get_gs_periods(self, table):
        self.connection, self.cursor = self.check_connection()
        if self.connection and self.cursor:
            try:
                result = self.cursor.execute("SELECT gs_id, gs_name FROM {table_name}".format(table_name=table)).fetchall()
                return result
            except sqlite3.Error as e:
                print("Ошибка SQLite:", e)
            finally:
                if self.cursor:
                    self.cursor.close()
                if self.connection:
                    self.connection.close()
