import mqtt_lib
import message
import asyncio


async def publish_async(data_size, break_amount, verbose):
    """
    - publishes data to a topic via connection to a broker
    - connection is established asynchronously
    - standard name for topic and publisher ID
    """
    temp_data = message.data_maker(data_size)

    try:
        mqtt_pub = mqtt_lib.MQTT_Publish('publisher', 'mngmtRequests')
        await mqtt_pub.PublishMessages_Async(
            temp_data, break_amount=break_amount, verbose=verbose)
    except Exception as error:
        print(
            f'Could not publish messages on topic mngmtRequests\nIssue -> {error}')
    else:
        return 1


async def test():
    for it in range(10):
        print(f'This is publishing iteration {it}...')
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(publish_async(100, 1, 0))
