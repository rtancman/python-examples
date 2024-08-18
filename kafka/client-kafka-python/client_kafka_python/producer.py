import json
import random
from kafka import KafkaProducer


def key_serializer(key):
    return key.encode('utf-8')

def serializer(message):
    return json.dumps(message).encode('utf-8')

topic = 'topic-example'
producer = KafkaProducer(
    key_serializer=key_serializer,
    bootstrap_servers=['localhost:9092'],
)

for some_number in range(10):
    salt_id = random.random()
    message_key = f'key:{some_number}:{salt_id}'
    message_value = {'key': message_key, 'value': f'some value {some_number}'}
    producer.send(topic, key=f'{some_number}:{salt_id}', value=serializer(message_value))
    producer.flush()
