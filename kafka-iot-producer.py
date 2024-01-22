from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging
import time
import json
import random


# sensor simulator , integrate your real sensor data here    
def temperature_simulator():
    temperature = round(random.uniform(25,35),2)
    return temperature

def publish_to_broker():
    producer = KafkaProducer(bootstrap_servers=['localhost:9093'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    print("connected to broker")
    while True:
        try:
            keys = ["hall","kitchen","bedroom","studyroom"]
            print("sending data to kafka broker")
            for i in keys:
                payload = json.dumps({"temperature":temperature_simulator()})
                # print(type(json.dumps(payload).encode('utf-8')))
                producer.send("sample_topic",payload,key=i.encode())
                print(payload)
                time.sleep(5)
        except KafkaError as ke:
            print(ke)
if __name__=="__main__":
    publish_to_broker()