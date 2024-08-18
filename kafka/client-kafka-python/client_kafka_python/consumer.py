import json
from kafka import KafkaConsumer


def deserializer(message):
    return json.loads(message.decode('utf-8'))

topic = 'topic-example'
consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    group_id='python_cli_consumer',
    value_deserializer=deserializer,
)

consumer.subscribe([topic])
for message in consumer:
    print(message.key)
    print(message.value)