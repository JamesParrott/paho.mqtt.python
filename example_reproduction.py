import sys
import paho.mqtt.client as mqtt
from time import sleep
import logging

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

MQTT_TOPIC = "test"
MQTT_PUBLISH_QOS = 2
MQTT_SUBSCRIBE_QOS = 2

def on_message(client, userdata, message):

    logger.debug(f"received payload {message.payload.decode('utf-8')}, mid: {message.mid}")
    logger.debug(f" _out_messages {len(client._out_messages)}, _in_messages {len(client._in_messages)}, _inflight_messages {client._inflight_messages}")


mqttc = mqtt.Client(client_id="client")
mqttc.max_inflight_messages_set(20)
mqttc.max_queued_messages_set(0)
mqttc.enable_logger(logger)

mqttc.on_message = on_message
mqttc.connect("localhost", port=1883, keepalive=5)
mqttc.subscribe(MQTT_TOPIC, qos=MQTT_SUBSCRIBE_QOS)
mqttc.loop_start()

n = 0
while True:
    mqttc.publish(MQTT_TOPIC, n, MQTT_PUBLISH_QOS)
    n += 1
    sleep(1.0)