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
            connection = db.connect(self.dbFile)
        except db.Error as err:
            print(
                f'There was an issue while trying to connect to the database\n{err}')
            return -1
        else:
            return connection

    def checkDatabaseExists(self, db_file):
        db_files = os.listdir(self.dbdir)
        if(db_file in db_files):
            print('all good')
        else:
            print('no bueno')


def main():
    local_db = DB('test_DataBae.db')


if __name__ == "__main__":
    main()
