# python-examples: Apache Kafka

## How to run Kafka

```
docker-compose up -d
```

Basic commands:
```
# list topic
kafka-topics.sh --bootstrap-server localhost:9092 --list

# describe topic
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic topic-example

# producer
echo "hello kafka!" > topic-input.txt
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic-example < topic-input.txt

# consumer
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic-example --from-beginning

# delete topic
kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic topic-example
```