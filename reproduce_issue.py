from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.properties import Properties

# Payload Format Indicator (identifier 1) appears twice.
Properties(PacketTypes.PUBLISH).unpack(bytes([4, 1, 1, 1, 0]))