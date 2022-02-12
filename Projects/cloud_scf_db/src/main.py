import db_tools

import message

import mqtt_lib

import constantParams as params


def main():
    db_file = params.LOCAL_DATABASE
    dump_file = params.LOCAL_DUMPFILE

    # new_db = db_tools.DB(local_db)
    # new_db.WriteData(data, write_mode='clean')
    # new_db.ReadDB(dump_file, to_file=1)

    mqtt_sub = mqtt_lib.MQTT_Subscribe(params.SUBSCRIBER, params.TOPIC)
    mqtt_sub.Subscribe()


if __name__ == '__main__':
    main()
