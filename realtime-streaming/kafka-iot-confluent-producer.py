
from confluent_kafka import Producer,KafkaException
import logging
import time
import json
import random


def temperature_simulator():
    temperature = round(random.uniform(25,35),2)
    return temperature

def read_ccloud_config(config_file):
    omitted_fields = set(['schema.registry.url', 'basic.auth.credentials.source', 'basic.auth.user.info'])
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                if parameter not in omitted_fields:
                    conf[parameter] = value.strip()
    return conf

def publish_to_broker():
    # make sure client.properties file downloaded from the confluent cloud is located in this folder 
    producer = Producer(read_ccloud_config("client.properties"))
    while True:
            try:
                keys = ["hall","kitchen","bedroom","studyroom"]
                print("sending data to kafka broker")
                for i in keys:
                    payload = json.dumps({"temperature":temperature_simulator()})
                    # print(type(json.dumps(payload).encode('utf-8')))
                    producer.produce("topic_0",value=payload,key=i.encode())
                    print(payload)
                    time.sleep(10)
            except KafkaException as ke :
                print(ke)
# producer.produce("topic_0", key="test", value="test1")
# producer.flush()
if __name__=="__main__":
    publish_to_broker()