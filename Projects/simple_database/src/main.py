import os

import time

from timeit import default_timer

import sqlite3 as db


def average(array):
    summ = sum(array)
    return float(summ / len(array))


class DB:
    DATA_Directory = '../db/'

    def __init__(self, database_name, table_name):
        self.dbdir = DB.DATA_Directory
        self.dbFile = database_name
        self.dbPath = f'{DB.DATA_Directory}{database_name}'
        self.tableName = table_name

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

    def createTable(self):
        # check first if the database exists in the proper directory
        if self.checkDatabaseExists(self.dbFile) != 1:
            db_object = self.createConnection()
        else:
            db_object = self.createConnection()

        # establish connection with the database and return the full connection object and the connection status

        # stop of there are issues with the database connection
        if db_object["status"] == -1:
            print('The database has connection issues')
            return

        db_conn = db_object["conn"]

        # create a cursors object that can execute SQL commands
        cursor = db_conn.cursor()

        # perform the creation of the actual table
        cursor.execute(f''' CREATE TABLE IF NOT EXISTS {self.tableName}
                            (array text, size int,average real)''')
        db_conn.commit()

        return db_object

    def addData(self, data):
        db_object = self.createTable()

        # prepare the data that will be added in the table
        data = data[0]
        avg = average(data)

        # open the database connection
        db_conn = db_object["conn"]
        # initialize the cursor
        cursor = db_conn.cursor()

        for _ in range(3):
            cursor.execute(
                f'INSERT INTO {self.tableName} VALUES (\f\'{data}\',{len(data)},{avg})')
        db_conn.commit()
        db_conn.close()


def main():
    local_db = DB('test_DataBae.db', 'Arrays')
    data = [[1, 2, 3] for _ in range(3)]
    local_db.addData(data)


if __name__ == "__main__":
    main()
