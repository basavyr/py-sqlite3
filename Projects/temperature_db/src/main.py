
import os

import temp as temp
import db_temps as DB


def getTopic():
    return f'ROOM_TEMPERATURE'


def getDBname():
    return f'room_temp.db'


def main():
    database_name = getDBname()
    topic = getTopic()
    # the table name must correspond to the topic
    table_name = topic

    # generate temperatures
    temps = temp.Room_Temp(20, 5)
    temp_list = temps.generateRoomTemps()

    # create database for storing the temps
    db = DB.DB()
    db.CreateTable(database_name, table_name)


if __name__ == '__main__':
    main()
