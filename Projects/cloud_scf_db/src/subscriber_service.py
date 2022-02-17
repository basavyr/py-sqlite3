import mqtt_lib

mqtt_sub = mqtt_lib.MQTT_Subscribe('subscriber', topic='mngmtRequests')
mqtt_sub.Subscribe(break_amount=5)
