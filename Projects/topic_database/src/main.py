import sqlite3

import os

import time

from timeit import default_timer

from random import randrange


def getTopic():
    return f'Bishu1'


class DB:
    DataStorePath = '../db/'
    db_proper_path = lambda db_file: f'{DB.DataStorePath}{db_file}'

    def __init__(self, db_name):
        self.dbName = db_name
        self.dbFile = f'{DB.DataStorePath}{db_name}'

    def createConnection(self, db_file):
        # the argument db_file is just the name of the database
        # file name must be appended with the proper path with the directory where all the databases are stored
        database_file = DB.db_proper_path(db_file)
        try:
            # connection should be made with a database within the proper location
            connection = sqlite3.connect(database=database_file)
        except sqlite3.Error as err:
            print('There was an issue with the connection to the database')
            return -1
        else:
            return connection

    def check_db_exists(self, db_file):
        db_files = os.listdir(DB.DataStorePath)
        if db_file in db_files:
            return 1
        return -1

    def dataInserter(self, cursor, data):
        return data

    def createTable(self, db_file, table_name):
        try:
            assert self.check_db_exists(db_file) == 1
        except AssertionError as err:
            print('Database does not exist but will create a new one')
            conn = self.createConnection(db_file)
        else:
            conn = self.createConnection(db_file)

        cursor = conn.cursor()

        cursor.execute(f'''CREATE TABLE {table_name}
                            (msg_id int, msg str, msg_size int, msg_avg float, timestamp str)''')

        # commit changes
        conn.commit()

        # close the connection
        conn.close()


def main():
    table_name = getTopic()

    db = DB('topic_data.db')
    db.createTable(db.dbName, table_name)


if __name__ == '__main__':
    main()
