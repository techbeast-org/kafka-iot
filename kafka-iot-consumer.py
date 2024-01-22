from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
     group_id=None,
     bootstrap_servers=['localhost:9092'], # bootstrap server
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     consumer_timeout_ms=1000,
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))
consumer.subscribe(['iot.telemetry.temperature'])

print('Receiving message...')
while True:
    print("print...")
    for messages in consumer:
        print(messages)