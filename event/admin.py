from django.contrib import admin
from .models import EventModel , EventUserModel

# Register your models here.

admin.site.register(EventModel)
admin.site.register(EventUserModel)