from kafka import KafkaAdminClient

admin_client = KafkaAdminClient(bootstrap_servers='localhost:9093')
topic_list = admin_client.list_topics()

print("Topics in the Kafka cluster:")
for topic in topic_list:
    print(topic)
