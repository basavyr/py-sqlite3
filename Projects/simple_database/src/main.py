import os

import time

from timeit import default_timer

import sqlite3 as db


class DB:
    DATA_Directory = '../db/'

    def __init__(self, database_name):
        self.dbdir = DB.DATA_Directory
        self.dbFile = database_name
        self.dbPath = f'{DB.DATA_Directory}{database_name}'

    def createConnection(self):
        try:
            connection = db.connect(self.dbPath)
        except db.Error as err:
            print(
                f'There was an issue while trying to connect to the database\n{err}')
            return {"conn": -1, "status": 0}
        else:
            return {"conn": connection, "status": 1}

    def checkDatabaseExists(self, db_file):
        db_files = os.listdir(self.dbdir)
        if(db_file in db_files):
            return 1
        return -1

    def createTable(self, table_name):
        # check first if the database exists in the proper directory
        if self.checkDatabaseExists(self.dbFile) != 1:
            return

        # establish connection with the database and return the full connection object and the connection status
        db_object = self.createConnection()

        # stop of there are issues with the database connection
        if db_object["status"] == -1:
            print('The database has connection issues')
            return

        db_conn = db_object["conn"]

        


def main():
    local_db = DB('test_DataBae.db')
    local_db.createTable('arrays')


if __name__ == "__main__":
    main()
