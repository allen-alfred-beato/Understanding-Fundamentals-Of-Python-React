from connection.conn import Database

class OrderModel:
    connection = Database.get_connection()
    cursor = connection.cursor()
    
    def __init__(self):
        pass
    