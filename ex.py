# import paho.mqtt.client as mqtt

# def on_message(client, userdata, msg):
#     print(f"Received: {msg.payload} on {msg.topic}")

# client = mqtt.Client(transport="websockets")
# client.on_message = on_message

# client.connect("test.mosquitto.org", port=8080, keepalive=60)

# client.subscribe("test/#")
# client.loop_forever()

import paho.mqtt.client as mqtt
import time

client = mqtt.Client(transport="websockets")
client.connect("test.mosquitto.org", port=8080, keepalive=60)

client.publish("test/topic", "Hello WebSocket MQTT!")
client.disconnect()