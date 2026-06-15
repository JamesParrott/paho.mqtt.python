import paho.mqtt.client as mqtt

TOPIC = "test/topic"


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Sender")
client.connect("localhost", 1883)
payload = b"Hello from sender!" + b"x" * (100 * 1024 * 1024)
msg = client.publish(TOPIC, payload, qos=0)
client.loop_forever()

