import sqlite3

import os

import time

from timeit import default_timer

from random import randrange

import messages as messages
import data as data


def getTopic():
    """
    - retrieves the name of a topic on which the client is subscried
    """
    return f'Bishu1'


def getNumberOfMessages():
    """
    - sets the number of messages to be pulled to a predefined constant value
    """
    pulling_messages = 100
    return pulling_messages


def set_database_name(topic):
    return f'{topic}_data.db'


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

    def insertData(self, db_file, table_name, message_data):
        conn = self.createConnection(db_file)
        cursor = conn.cursor()
        for data_element in message_data:
            stringified_data = messages.Message.stringifyDM(data_element)
            stringified_data_id = (
                1, stringified_data[0], stringified_data[1], stringified_data[2], stringified_data[3])
            print(stringified_data_id)
            cursor.execute(
                f'INSERT INTO {table_name} VALUES (?,?,?,?,?)', stringified_data_id)

        conn.commit()

        conn.close()

    def createTable(self, db_file, table_name):
        try:
            assert self.check_db_exists(db_file) == 1
        except AssertionError as err:
            print('Database does not exist but will create a new one')
            conn = self.createConnection(db_file)
        else:
            conn = self.createConnection(db_file)

        cursor = conn.cursor()

        # temporary chain to string for the entire database
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                            (msg_id int, msg str, msg_size str, msg_avg str, timestamp str)''')

        # commit changes
        conn.commit()

        # close the connection
        conn.close()

    def getCursor(self, db_file):
        # establish the connection with the database
        conn = self.createConnection(db_file)

        # create the cursor
        cursor = conn.cursor()

        return cursor

    def pullData(self):
        """
        - method used for pulling a set of messages using the messager class
        - the pulled messages will be used within the database
        - the list of messages (actual data) is represented by an array of randomly generated arrays and some specific objects attached to them
        - the number of messages is set from the class initialization
        """

        # generate the random data
        data_object = data.Data()
        random_data = data_object.GiveRandomData()

        # integrate the randomly generated data into messages
        dms = messages.Message(random_data)
        public_msgs = dms.CreateMessages()

        return public_msgs


def main():
    table_name = getTopic()
    number_of_messages = getNumberOfMessages()
    database_name = set_database_name(getTopic())

    db = DB(database_name)
    db.createTable(database_name, table_name)

    messages = db.pullData()

    cursor = db.getCursor(database_name)

    db.insertData(database_name, table_name, messages)


if __name__ == '__main__':
    main()
