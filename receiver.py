import paho.mqtt.client as mqtt

TOPIC = "test/topic"

def on_connect(client, userdata, flags, reason_code, properties=None):
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload
    print(f"Received: {payload[:18]}, ...,(length {len(payload)}) on {msg.topic}")

def on_disconnect(client, userdata, flags, reason_code, properties):
    print("Disconnected, reason:", reason_code)
    print("Already received", len(client._in_packet['packet']) )


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# client.connect("localhost", 1883, keepalive=30)
client.connect("192.168.137.1", 1883, keepalive=4)
client.loop_forever()
