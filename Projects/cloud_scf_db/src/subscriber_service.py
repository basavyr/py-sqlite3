import mqtt_lib
import asyncio


async def subscribe_async(break_amount):

    try:
        mqtt_sub = mqtt_lib.MQTT_Subscribe('subscriber', topic='mngmtRequests')
        mqtt_sub.Subscribe(break_amount=break_amount)
    except Exception as error:
        print(
            f'There was an issue while subscription was ON\nIssue -> {error}')
    else:
        return 1
