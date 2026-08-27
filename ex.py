from paho.mqtt.client import topic_matches_sub

# Per MQTT 3.1.1/5.0 §4.7.1.2 these must both be True.
assert topic_matches_sub("sport/#", "sport")
assert topic_matches_sub("/#", "/")

print("Tests passed.")