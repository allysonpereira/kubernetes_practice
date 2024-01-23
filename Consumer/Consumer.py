import paho.mqtt.client as mqtt
import sys
import logging
import json
import mysql.connector

# Define the logger before using it
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mydb = mysql.connector.connect(
    host="10.4.5.16",
    user="testuser",
    password="pass",
    database="test_schema"
)

mycursor = mydb.cursor()

def on_message(client, userdata, message):
    try:
        payload = message.payload.decode()
        
        sql = "INSERT INTO test_table2 (Content) VALUES (%s)"
        val = (payload,)
        mycursor.execute(sql, val)
        mydb.commit()

    except Exception as e:
        logger.error(f"Error inserting message into the database: {e}")

with open("myjson.json", "r") as json_file:
    json_data = json.load(json_file)

broker_address = json_data.get("broker_address", "localhost")
port = json_data.get("port", 1883)
topic = json_data.get("topic", "test/topic")

client = mqtt.Client("C1")
client.on_message = on_message

if client.connect(broker_address, port) != 0:
    logger.error("Could not connect to MQTT broker.")
    sys.exit(-1)

client.subscribe(topic)

try:
    logger.info("Press CTRL+C to exit")
    logger.info("Connected to broker")
    client.loop_forever()
except KeyboardInterrupt:
    logger.info("Disconnected from broker")
    client.disconnect()
