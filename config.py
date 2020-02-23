

import os


DATA_DIR = os.path.normpath("C:\\Users\\allen\datasets\\commerce_data")

TABLES = {
    '_'.join(table_name.split("_")[1:-1]) : os.path.join(DATA_DIR, table_name) for table_name in os.listdir(DATA_DIR)
}


