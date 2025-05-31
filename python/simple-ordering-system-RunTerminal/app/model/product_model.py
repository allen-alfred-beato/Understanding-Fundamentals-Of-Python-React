from connection.conn import Database


class Product:
    def __init__(self, cls):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        
    