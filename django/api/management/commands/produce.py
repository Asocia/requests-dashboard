import asyncio
import json
from django.core.management.base import BaseCommand
from kafka import KafkaProducer


def value_serializer(value):
    return json.dumps(value).encode("utf8")


producer = KafkaProducer(
    bootstrap_servers=["kafka:29092"], value_serializer=value_serializer
)


PERIOD = 0.5
header = ["type", "response_time", "timestamp"]


async def readline(f):
    while True:
        data = f.readline()
        if data:
            return data[:-1]
        await asyncio.sleep(PERIOD)


async def test():
    with open("api.log") as f:
        dummy_data = dict(zip(header, ["GET", "0", "1617539865"]))
        producer.send("requests", value=dummy_data)
        while True:
            line = await readline(f)
            data = dict(zip(header, line.split(",")))
            producer.send("requests", value=data)
            print(f"producer: {data}")


class Command(BaseCommand):
    help = "Watch log file and send messages to kafka"

    def handle(self, *args, **options):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test())
