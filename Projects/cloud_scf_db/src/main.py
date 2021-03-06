import db_tools

import message

import mqtt_lib

import constantParams as params


def main():
    db_file = params.LOCAL_DATABASE
    dump_file = params.LOCAL_DUMPFILE

    # create the database object that will be used for created databases and tables
    new_db = db_tools.DB(local_db)

    data = message.data_maker(150)

    # the clean flag for write_mode argument means that the table within the database must be empty before adding data to it
    new_db.WriteData(data, write_mode='clean')

    # the to_file flag tells that the read information within the database should be dumped into an external file
    new_db.ReadDB(dump_file, to_file=1)

    # check the database with a certain OS value
    # new_db.SelectByOS('macOS')

    mqtt_sub = mqtt_lib.MQTT_Subscribe(params.SUBSCRIBER, params.TOPIC)
    mqtt_sub.Subscribe()

async def main():
    data_size = 100
    break_amount = 1
    verbose_mode = 0
    H = await asyncio.gather(
        publisher_service.publish_async(data_size, break_amount, verbose_mode),
        subscriber_service.subscribe_async(
            break_amount * data_size, verbose_mode),
    )
    print(H)

if __name__ == '__main__':
    asyncio.run(main())
    # writeDatabase()
