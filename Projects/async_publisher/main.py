import paho.mqtt.client as mqtt
import time

# run pipenv shell for executing python module with the paho package

host0 = 'broker.hivemq.com'


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
    main()
