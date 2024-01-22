from kafka import KafkaAdminClient
from kafka.admin import NewTopic

admin_client = KafkaAdminClient(bootstrap_servers='localhost:9093')
topic_list = admin_client.list_topics()
# topic_list = []
# topic_list.append(NewTopic(name="sample_topic", num_partitions=1, replication_factor=1))
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

print("Topics in the Kafka cluster:")
for topic in topic_list:
    print(topic)
