import paho.mqtt.client as mqtt

TOPIC = "test/topic"

# def on_connect(client, userdata, flags, reason_code, properties=None):
#     payload = b"x" * (100 * 1024 * 1024)
#     msg = client.publish(TOPIC, payload, qos=1)

# def main():
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# client.on_connect = on_connect
client.connect("localhost", 1883)
payload = b"Hello from sender!"  + b"x" * (100 * 1024 * 1024)
msg = client.publish(TOPIC, payload, qos=1)
client.loop_forever()

# if __name__ == '__main__':
#     main()