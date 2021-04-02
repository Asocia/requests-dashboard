import json

from django.core.management.base import BaseCommand
from kafka import KafkaConsumer


def value_deserializer(value):
    return json.loads(value.decode('utf8'))


class Command(BaseCommand):
    help = 'Consume messages and write them to database'

    def handle(self, *args, **options):
        consumer = KafkaConsumer(
            'requests',
            bootstrap_servers=['kafka:29092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            api_version=(0, 11, 5),
            value_deserializer=value_deserializer
        )

        for event in consumer:
            event_data = event.value
            # Do whatever you want
            self.stdout.write(self.style.SUCCESS(f'consumer: {event_data}'))
