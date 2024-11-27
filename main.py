from database_connection import DatabaseConnection
import threading

def worker():
    db = DatabaseConnection()
    print(db.get_connection())

if __name__ == "__main__":
    threads = []

    # Создаем несколько потоков, чтобы проверить, что Singleton работает
    for i in range(5):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()