from controller.ordering_processes import Order
from connection.conn import Database
from view.order_screen import *
from utils.utils import Utilities


def main():
    print("Starting...")
    Database.initialize_connection("cb_db.db")    

if __name__ == "__main__":
    main()
    
    