import mqtt_lib
import asyncio


async def subscribe_async(break_amount, verbose):

    try:
        mqtt_sub = mqtt_lib.MQTT_Subscribe('subscriber', topic='mngmtRequests')
        await mqtt_sub.Subscribe(break_amount=break_amount, verbose=verbose)
    except Exception as error:
        print(
            f'There was an issue while subscription was ON\nIssue -> {error}')
    else:
        return 1


async def test():
    for it in range(10):
        print(f'This is subscribing iteration {it}...')
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(subscribe_async(100, 0))
