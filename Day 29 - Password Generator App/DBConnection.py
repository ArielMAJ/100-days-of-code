import sqlite3
from sqlite3 import Error


def create_connection(database_file_path):
    connection = None
    try:
        connection = sqlite3.connect(database_file_path)
    except Error as error_msg:
        print(error_msg)
    return connection


def insert_data_into_DB(db_connection, values):
    sql ='''INSERT INTO PASSWORDS(WEBSITE,USERNAME,PASSWORD)
            VALUES(?,?,?)'''
    with db_connection:
        cursor = db_connection.cursor()
        cursor.execute(sql, values)
        db_connection.commit()