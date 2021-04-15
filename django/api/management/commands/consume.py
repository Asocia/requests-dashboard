import json

from django.core.management.base import BaseCommand
from django.utils import timezone
from kafka import KafkaConsumer
from api.models import Request


def value_deserializer(value):
    return json.loads(value.decode("utf8"))


class Command(BaseCommand):
    help = "Consume messages and write them to database"

    def handle(self, *args, **options):
        consumer = KafkaConsumer(
            "requests",
            bootstrap_servers=["kafka:29092"],
            value_deserializer=value_deserializer,
        )

        tz = timezone.get_current_timezone()
        for event in consumer:
            dt = timezone.datetime.fromtimestamp(int(event.value["timestamp"]), tz=tz)
            data = {**event.value, "datetime": dt}
            del data["timestamp"]
            Request.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f"consumer: {data}"))
