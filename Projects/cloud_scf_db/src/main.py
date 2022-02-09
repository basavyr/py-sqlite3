import db_tools

import message

import mqtt_lib


def main():
    local_db = '../db/management_requests.db'
    dump_file = '../db/exported_db.dat'

    # new_db = db_tools.DB(local_db)
    # new_db.WriteData(data, write_mode='clean')
    # new_db.ReadDB(dump_file, to_file=1)

    mqtt_sub = mqtt_lib.MQTT_Subscribe('subscriber', 'mngmtRequests')
    mqtt_sub.Subscribe()


if __name__ == '__main__':
    main()
