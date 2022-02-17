import db_tools

import message

import mqtt_lib


def main():
    local_db = '../db/management_requests.db'
    dump_file = '../db/exported_db.dat'

    data = message.data_maker(10)

    # create the database object that will be used for created databases and tables
    new_db = db_tools.DB(local_db)

    # the clean flag for write_mode argument means that the table within the database must be empty before adding data to it
    new_db.WriteData(data, write_mode='dirty')
    # the to_file flag tells that the read information within the database should be dumped into an external file
    new_db.ReadDB(dump_file, to_file=1)
    # check the database with a certain OS value
    new_db.SelectByOS('macOS')

    # mqtt_sub = mqtt_lib.MQTT_Subscribe('subscriber', 'mngmtRequests')
    # mqtt_sub.Subscribe()


if __name__ == '__main__':
    main()
