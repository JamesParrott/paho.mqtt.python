import paho.mqtt.client as mqtt

TOPIC = "test/topic"
import inspect


def get_caller_name():
    frame = inspect.currentframe()
    caller_frame = frame.f_back.f_back
    return caller_frame.f_code.co_name

def my_function():
    print(f"Called by: {get_caller_name()}")

def another_function():
    my_function()
another_function()  # Output: Called by: another_function

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_log = print
client.connect("localhost", 1883)
payload = b"Hello from sender!" + b"x" * (100 * 1024 * 1024 * 2)
msg = client.publish(TOPIC, payload, qos=0)
# while True:
client.loop()
# while True:
    # client.loop()
# client.loop_forever()

