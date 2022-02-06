
import os

import temp as temp
import db_temps as DB
import graph_temps as grafx


def getTopic():
    return f'ROOM_TEMPERATURE'


def getDBname():
    return f'room_temp.db'


def main():
    database = getDBname()
    topic = getTopic()
    # the table name must correspond to the topic
    table = topic

    # generate temperatures
    temp_cls = temp.Room_Temp(20, 5)
    temps = temp_cls.generateRoomTemps()
    # plot temps
    gfx = grafx.Graph()
    gfx.PlotData(temps, 'temps_outside.pdf')

    # create database for storing the temps
    db = DB.DB()
    db.CreateTable(database, table)
    db.InsertData(temps, database, table)
    db.SelectData(database, table)


if __name__ == '__main__':
    main()
