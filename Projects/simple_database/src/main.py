import os

import time

from timeit import default_timer

import sqlite3 as db

from random import randrange


def average(array):
    summ = sum(array)
    return round(float(summ / len(array)), 3)


def generateArrays(n_arrays):
    ret_arrays = []
    for idx in range(n_arrays):
        idx_array = [randrange(0, 100) for _ in range(randrange(1, 10))]
        ret_arrays.append(idx_array)
    return ret_arrays


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

        # open the database connection
        db_conn = db_object["conn"]
        # initialize the cursor
        cursor = db_conn.cursor()

        for data_idx in data:
            cursor.execute(
                f'INSERT INTO {self.tableName} VALUES (\f\'{data_idx}\',{len(data_idx)},{average(data_idx)})')

        db_conn.commit()

        db_conn.close()

    def selectData(self):
        db_object = self.createConnection()

        if(db_object["status"] == -1):
            print('Issue with the database connection')
            return

        db_conn = db_object["conn"]

        cursor = db_conn.cursor()

        # this retrieves all the entries within the database that correspond to the query
        selected_data = cursor.execute(
            f'''SELECT * FROM {self.tableName} WHERE size = 7''')

        # this fetches the selected data and makes it avaliable to python as an object
        my_data = selected_data.fetchall()
        for data in my_data:
            print(data)

        # db_conn.commit()
        db_conn.close()

    def getDBsize(self):
        db_object = self.createConnection()
        db_conn = db_object["conn"]

        cursor = db_conn.cursor()

        db_size = len(cursor.execute(
            f'SELECT * FROM {self.tableName}').fetchall())

        print(db_size)


def main():
    local_db = DB('test_DataBae.db', 'Arrays')
    data = generateArrays(10)
    local_db.getDBsize()
    # local_db.addData(data)
    # local_db.selectData()


if __name__ == "__main__":
    main()
