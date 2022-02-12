import mqtt_lib

import constantParams as params

import message


temp_data = message.data_maker(100000)


mqtt_pub = mqtt_lib.MQTT_Publish(params.PUBLISHER, params.TOPIC)
mqtt_pub.PublishMessages_Async(temp_data, verbose=0)
