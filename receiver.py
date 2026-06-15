import paho.mqtt.client as mqtt

TOPIC = "test/topic"

class Client(mqtt.Client):
    def _do_on_disconnect(self, *args, **kwargs):
        print(f" _do_on_disconnect called: {args}, {kwargs}")
        super()._do_on_disconnect(*args, **kwargs)

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
client.on_log = print

# client.connect("localhost", 1883, keepalive=30)
client.connect("192.168.137.1", 1883, keepalive=10)
#while client.is_connected:
#    client.loop_read()

client.loop_forever()
