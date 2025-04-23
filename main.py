import os

from db.create_tables import *
from db.insert_values import *
from db.repository import *
from resources.menu import main_menu

def main():
    if not os.path.exists("Alessio_charity_donations.db"):
        createTable()
        insertValue()

    main_menu()

# If the main.py file is imported into other modules, 
# it will not be executed because the __name__ will not be __main__. 
# Instead, it will have the name of the module where it was imported.
if __name__ == "__main__":
    main()
