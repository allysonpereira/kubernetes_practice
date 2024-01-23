import paho.mqtt.client as mqtt
import time
import logging
import json

with open("myjson.json", "r") as json_file:
        json_data = json.load(json_file)

broker_address = json_data.get("broker_address" , "localhost")
port = json_data.get("port" , 1883)
topic = json_data.get("topic" , "test/topic")

#broker_address = "localhost"
#port = 1883
#topic = "test/topic"

client = mqtt.Client("P1")
client.connect(broker_address, port)

while True:
    message = "Hello from mqtt but with docker and kubernetes now!"
    ret = client.publish(topic, message)
    time.sleep(1)