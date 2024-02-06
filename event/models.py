from django.db import models
from core.models import user
# Create your models here.


class EventModel(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    event_maker = models.ForeignKey(user , on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"

class EventUserModel(models.Model):
    event_picker = models.ForeignKey(user , on_delete=models.CASCADE , default = None)
    event = models.ManyToManyField(EventModel)

    def __str__(self) -> str:
        return f"{self.event}"