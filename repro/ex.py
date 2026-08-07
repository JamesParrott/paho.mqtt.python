# To start Mosquitto:
# "c:\Program Files\Mosquitto\mosquitto.exe" -v -c repro\mosquitto.conf

import logging
import sys

import paho.mqtt.client as mqtt

HOST = "test.mosquitto.org" if sys.argv[1:2] == ["false"] else "localhost"

print(f"{HOST=}")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def on_publish(client, userdata, mid, rc, properties):
    print("Published")
    client.disconnect()

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5, transport="websockets")
mqtt_client.enable_logger()
mqtt_client.on_publish = on_publish
mqtt_client.connect(HOST, 8080, 60)

msg = b"a"*1_000 # Got: aa
msg = b"b"*5_000 # Got: bbbbbbb
msg = b"c"*10_000 # Got: ccccccccccccccccccccccccccccc
msg = b"d"*15_000 # Got: ddddddddddddddddddddddddddddddddddddddddddddddddddddddd
msg = b"e"*15_000 # Got: nada
# upload_test

msg = b"f"*132096

result = mqtt_client.publish("upload_test", msg)
mqtt_client.loop_forever()
