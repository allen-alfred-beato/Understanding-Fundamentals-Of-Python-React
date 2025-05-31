import sqlite3


class Database:
    _connection = None
    _database_path = None

    @classmethod
    def initialize_connection(cls, database):
        cls._database_path = database
        if cls._connection is None:
            cls._connection = sqlite3.connect(database)
            cls._connection.row_factory = sqlite3.Row
            if cls._connection:
                print("Database Initailized!")
            

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            if cls._database_path is None:
                raise ValueError("Database Initialization Failed!")
            cls._connection = sqlite3.connect("cb_db.db")
            cls._connection.row_factory = sqlite3.Row 
            
        return cls._connection
    
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls.get_connection = None