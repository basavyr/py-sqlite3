import paho.mqtt.client as mqtt

import paho.mqtt.publish as publisher

import helper_tools

import constantParams as params

import time

import message as msg

import asyncio


def on_publish_callback(client, userdata, mid):
    print(f'Published to the broker with mid -> {mid}')


def on_connect_callback(client, userdata, flags, rc):
    print(f'Connected to the broker with rc -> {rc}')


def on_disconnect_callback(client, userdata, rc):
    print(f'Disconnected from the broker with rc -> {rc}')


def on_message_callback(client, userdata, message):
    encoded_message = message.payload
    decoded_message = encoded_message.decode('utf-8')
    # elements = decoded_message.strip()
    # print(elements[elements.find(','):elements.find('[') - 2])
    # print(elements[2:4])
    print(
        f'Received message {decoded_message} from broker on topic {message.topic}/')


class MQTT_Publish:
    HOST = 'broker.hivemq.com'

    def __init__(self, client_name, topic):
        self.client = client_name
        self.topic = topic

    def CreateClient(self):
        temp_client = mqtt.Client(client_id=self.client)

        # set additional callbacks for the client
        temp_client.on_connect = on_connect_callback
        temp_client.on_publish = on_publish_callback
        temp_client.on_disconnect = on_disconnect_callback

        return temp_client

    async def PublishMessages_Async(self, message_list, break_amount, verbose):
        """
        - use a custom connection with an arbitrary loop to publish messages to a broker
        - the client connects to the broker asynchronously, non-blocking operation
        - the data is published within a timed window (break_amount variable gives the time between two concurrent published messages)
        """
        temp_client = self.CreateClient()

        temp_client.connect_async(host=params.TOPIC)

       # ******************************* #
        temp_client.loop_start()

        for message in message_list:
            if(verbose == 1):
                print(f'Generated message -> {message}')

            # generate a pure string from the initial message
            dm = msg.stringify(message)

            # publish the message as a pure string
            temp_client.publish(self.topic, dm)

            if(verbose == 1):
                print(
                    f'Published message on topic {self.topic} via broker {MQTT_Publish.HOST}')
            await asyncio.sleep(break_amount)

        temp_client.loop_stop()
       # ******************************* #

        temp_client.disconnect()


class MQTT_Subscribe:
    HOST = 'broker.hivemq.com'

    def __init__(self, client_name, topic):
        self.client = client_name
        self.topic = topic

    def CreateClient(self):
        temp_client = mqtt.Client(client_id=self.client)

        # set additional callbacks for the client
        temp_client.on_connect = on_connect_callback
        temp_client.on_disconnect = on_disconnect_callback
        temp_client.on_message = on_message_callback

        return temp_client

    async def Subscribe(self, break_amount, verbose):
        """
        - create a client that will subscribe to a topic
        - client will connect to the broker which listens to any incoming messages for that particular topic
        """

        temp_client = self.CreateClient()

        temp_client.connect(host=params.BROKER)

        temp_client.subscribe(topic=self.topic)

        # # generate a non blocking way of connecting to the broker and establishing the connection loop
        if(verbose == 1):
            print('Starting the subscription loop...')
        temp_client.loop_start()

        await asyncio.sleep(break_amount)

        if(verbose == 1):
            print('Stopping the subscription loop...')
        temp_client.loop_stop()

        temp_client.disconnect()
