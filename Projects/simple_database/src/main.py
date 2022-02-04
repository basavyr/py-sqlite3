import os

import time

from timeit import default_timer

import sqlite3 as db


class DB:
    def __init__(self, database_name):
        self.dbFile = database_name

    def createConnection(self):
        try:
            connection = db.connect(self.dbFile)
        except db.Error as err:
            print(
                f'There was an issue while trying to connect to the database\n{err}')
            return -1
        else:
            return connection


def main():
    local_db = DB('../db/test_DataBae.db')
    local_db.createConnection()


if __name__ == "__main__":
    main()
