import paho.mqtt.client as mqtt
import time
import asyncio

# run pipenv shell for executing python module with the paho package

host0 = 'broker.hivemq.com'


async def printNumber(number):
    await asyncio.sleep(2)
    print(number)


def main():
    client1 = mqtt.Client('publihser')

    message = 'This is a message'

    print('this is before async connection')

    client1.connect_async(host=host0)

    print('this is after async connection')
    print('starting the loop')
    client1.loop_start()
    time.sleep(3)

    client1.loop_stop()


if __name__ == '__main__':
    # main()
    number=33
    printNumber(number)
    print(f' non async ->{number}')
