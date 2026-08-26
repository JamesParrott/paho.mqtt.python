from paho.mqtt.client import topic_matches_sub

# Per MQTT 3.1.1/5.0 §4.7.1.2 these must all be True,
# but the current implementation returns False:
assert topic_matches_sub("sport/#", "sport")     # False (bug)
assert topic_matches_sub("/#", "/")              # False (bug)