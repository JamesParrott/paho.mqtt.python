import logging
import paho.mqtt.publish as publish

logging.basicConfig(level=logging.DEBUG)
publish.single("paho/test", "hello", hostname="127.0.0.1", port=18830)
print("message published")