# my_singleton_project/tests/test_database.py

import pytest
from database_connection import DatabaseConnection

class TestDatabaseConnection:

    def test_singleton(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        assert db1 is db2  # Проверяем, что оба экземпляра равны

    def test_connection_message(self):
        db = DatabaseConnection()
        assert db.get_connection() == 'Database Connection Established'

    def test_instance_type(self):
        db = DatabaseConnection()
        assert isinstance(db, DatabaseConnection)

    def test_multiple_instances(self):
        instances = [DatabaseConnection() for _ in range(10)]
        assert all(instance is instances[0] for instance in instances)

    def test_singleton_property(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        assert id(db1) == id(db2)  # Проверяем, что id у обоих экземпляров одинаковый

    def test_connection_not_none(self):
        db = DatabaseConnection()
        assert db.get_connection() is not None

    def test_connection_type(self):
        db = DatabaseConnection()
        assert isinstance(db.get_connection(), str)

    def test_different_calls(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        assert db1.get_connection() == db2.get_connection()  # Проверяем, что сообщения одинаковые

    def test_no_new_instance(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        assert db1 is db2  # Проверяем, что при повторном вызове не создается новый экземпляр
