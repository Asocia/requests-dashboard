from django.db import models


class Request(models.Model):
    type = models.CharField(max_length=6)
    response_time = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField()
    shown_in_graph = models.BooleanField(default=False)

    def __str__(self):
        return (
            f'{self.type} - {self.response_time} ms - {self.datetime.strftime("%H:%M")}'
        )
