# "c:\Program Files\Mosquitto\mosquitto.exe" -v -c repro\mosquitto.conf
# "c:\Program Files\Mosquitto\mosquitto_pub.exe" -t test1 -m Some-retained-message -r
from paho.mqtt.client import Client, SubscribeOptions, MQTTv5

client = Client(protocol=MQTTv5)
client.on_message=lambda c, ud, m: print(m.payload.decode())
client.connect("localhost", 1883)
qos=2
a = [("test1", SubscribeOptions(qos=qos)), ("test2", SubscribeOptions(qos=qos))]
client.subscribe(a)

client.loop_forever()
