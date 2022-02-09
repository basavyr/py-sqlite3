import paho.mqtt.client as mqtt

import paho.mqtt.publish as publisher

import helper_tools

import time


def on_publish_callback(client, userdata, mid):
    print(f'Published to the broker with mid -> {mid}')


def on_connect_callback(client, userdata, flags, rc):
    print(f'Connected to the broker with rc -> {rc}')


def on_disconnect_callback(client, userdata, rc):
    print(f'Disconnected from the broker with rc -> {rc}')


def on_message_callback(client, userdata, message):
    print(
        f'Received message {message.payload} from broker on topic {message.topic}/')


class MQTT_Publish:
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

    def PublishMessages_Async(self, message_list, verbose):
        """
        - use a custom connection with an arbitrary loop to publish messages to a broker
        """
        temp_client = self.CreateClient()

        temp_client.connect_async(host='broker.hivemq.com')

       # ******************************* #
        temp_client.loop_start()

        for message in message_list:
            if(verbose == 1):
                print(message)
            temp_client.publish(self.topic, message)
            time.sleep(2)

        temp_client.loop_stop()
       # ******************************* #

        temp_client.disconnect()


class MQTT_Subscribe:
    def __init__(self, client_name, topic):
        self.client = client_name
        self.topic = topic

    def CreateClient(self):
        temp_client = mqtt.Client(client_id=self.client)

        # set additional callbacks for the client
        temp_client.on_connect = on_connect_callback
        temp_client.on_publish = on_publish_callback
        temp_client.on_disconnect = on_disconnect_callback
        temp_client.on_message = on_message_callback

        return temp_client

    def Subscribe(self):
        temp_client = self.CreateClient()

        temp_client.connect(host='broker.hivemq.com')

        temp_client.subscribe(topic=self.topic)

        temp_client.loop_forever()
