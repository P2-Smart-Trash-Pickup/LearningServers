import sys

import paho.mqtt.client as paho

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)
topic=input("topic: ")
client.publish(topic, "Hi, paho mqtt client works fine!", 0)
client.disconnect()