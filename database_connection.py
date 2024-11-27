# database_connection.py
from singleton_meta import SingletonMeta
import time

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        time.sleep(1)  # Имитация времени подключения
        return "Database Connection Established"

    def get_connection(self):
        return self.connection
