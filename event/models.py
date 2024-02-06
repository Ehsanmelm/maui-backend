from django.db import models
from core.models import UserModel
# Create your models here.


class EventModel(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    event_maker = models.ForeignKey(UserModel , on_delete = models.CASCADE)

    # created_at = models.DateField(auto_now_add = True)

    capacity = models.PositiveIntegerField(default = None)
    location = models.CharField(max_length = 255 , default = None)



    def __str__(self) -> str:
        return f"{self.title}"

class EventUserModel(models.Model):
    event_picker = models.ForeignKey(UserModel , on_delete=models.CASCADE , default = None)
    event = models.ManyToManyField(EventModel)

    def __str__(self) -> str:
        return f"{self.event}"