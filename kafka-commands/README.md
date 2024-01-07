## List of useful Kafka commands


# Logging into the Kafka Container
```bash
docker exec -it broker01 /bin/bash
```

# Navigate to the Kafka Scripts directory
```bash
cd /opt/bitnami/kafka/bin

```

# Creating new Topics
```bash
   ./kafka-topics.sh --create --topic iot.telemetry.temperature --bootstrap-server broker01:29092 --partitions 1 --replication-factor 1
```
        

# Listing Topics
```bash
   ./kafka-topics.sh --bootstrap-server broker01:29092 --list
```
       

# Getting details about a Topic
```bash
   ./kafka-topics.sh --bootstrap-server broker01:29092 --describe
```
   


# Publishing Messages to Topics
```bash
   ./kafka-console-producer.sh --bootstrap-server broker01:29092 --topic iot.telemetry.temperature
```
      
# Consuming Messages from Topics
```bash
   ./kafka-console-consumer.sh --bootstrap-server broker01:29092 --topic iot.telemetry.temperature --from-beginning
```
     

# Deleting Topics
```bash
     ./kafka-topics.sh --bootstrap-server broker01:29092 --delete --topic iot.telemetry.temperature
```
   

# Create a Topic with multiple partitions
```bash
 ./kafka-topics.sh --bootstrap-server broker01:29092 --create --topic iot.telemetry.temperature --partitions 3 --replication-factor 1
```
       


# Check topic partitioning
```bash
 ./kafka-topics.sh -bootstrap-server broker01:29092 --topic iot.telemetry.temperature --describe
```
       

# Publishing Messages to Topics with keys
```bash
   ./kafka-console-producer.sh --bootstrap-server broker01:29092 --property "parse.key=true" --property "key.separator=:" --topic iot.telemetry.temperature
```
     

# Consume messages using a consumer group
```bash
    ./kafka-console-consumer.sh --bootstrap-server broker01:29092 --topic iot.telemetry.temperature --group test-consumer-group --property print.key=true --property key.separator=" = " --from-beginning
```
    

# Check current status of offsets
```bash
./kafka-consumer-groups.sh --bootstrap-server broker01:29092 --describe --all-groups

```
        
# Publish to the Topic with key
```bash
  ./kafka-console-producer.sh --bootstrap-server broker01:29092 --property "parse.key=true" --property "key.separator=:" --topic iot.telemetry.temperature
```
      

# Consume Message from the Topic
```bash
 ./kafka-console-consumer.sh --bootstrap-server broker01:29092 --topic iot.telemetry.temperature --group usecase-consumer-group --property print.key=true --property key.separator=" = " --from-beginning
```

