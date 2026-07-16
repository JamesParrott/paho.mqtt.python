"""mosquitto.conf

listener 1883 127.0.0.1
log_type all
allow_anonymous true

"""

""" Usage
#Session 1:
mosquitto -c mosquitto.conf
# Session 2:
python issue_894.py
# Session 3:
sudo iptables -I INPUT -p tcp -i lo --dport 1883 -j DROP
sudo iptables -D INPUT -p tcp -i lo --dport 1883 -j DROP
"""


import itertools
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Reconnecting...")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 4)
#client.connect("127.0.0.1", 1883, 60)
client.loop_start()

for i in itertools.count():
    client.publish("test/topic", f"Hello #{i}!")
    time.sleep(1)

client.loop_stop()
client.disconnect()