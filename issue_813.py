import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
def on_disconnected(_client, userdata, rc):
    global is_connected
    print(f"DISCONNECTED: {userdata=}, {mqtt.MQTTErrorCode(rc)=}")
    is_connected = False

client.on_disconnect = on_disconnected

# enable logging, let it create it's own logger
client.enable_logger(logger=None)

print("connecting...")
client.connect("localhost", 1883, keepalive=2)
# 
for _ in range(10):
    client.loop()
is_connected = client.is_connected()
print(f"{is_connected=}")

# print("starting loop...")
# client.loop_start()
# print("loop started")
# while True:
#     print("publishing message...")
#     client.publish("testtopic1", "hello world", qos=0)
#     time.sleep(0.5)

last_pub_time = 0
while is_connected:
    client.loop_misc()
    now = time.time()
    if now - last_pub_time > 0.5:
        print("publishing message...")
        # client.loop_write()
        client.publish("testtopic1", b"hello world", qos=1)
        last_pub_time = now
        # client.loop_read()