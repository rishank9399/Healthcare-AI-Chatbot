# db_operations.py


import pymysql

def get_connection():
    """Create a connection to the MySQL database."""
    return pymysql.connect(
        host="your-aiven-host",
        user="your-username",
        password="your-password",
        database="your-database",
        port=3306
    )
