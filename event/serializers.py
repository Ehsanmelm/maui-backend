from rest_framework import serializers
from .models import EventModel , EventUserModel 
from core.models import UserModel

class CreateEventSerializer(serializers.ModelSerializer):
    event_maker = serializers.CharField(read_only = True)
    class Meta:
        model = EventModel
        fields = '__all__'

    def create(self, validated_data):
        event_maker = UserModel.objects.get(id=self.context['id'])
        title = self.validated_data['title']
        description = self.validated_data['description']

        event = EventModel.objects.create(event_maker=event_maker , title=title , description=description)
        event.save()

        return event
    
class EventUserSerializer(serializers.ModelSerializer):
    event_picker = serializers.CharField(read_only =True)
    class Meta:
        model = EventUserModel
        fields = '__all__'
    
    # def create(self, validated_data):
    #     event_picker = user.objects.get(id = self.context['id'])
        
    #     # if 
    #     event = EventUserModel.objects.create(event_picker = event_picker , **validated_data)
    #     event.save()

    #     return event
    def create(self, validated_data):
        event_picker = UserModel.objects.get(id=self.context['id'])
        events_data = validated_data.pop('event', [])  # Remove 'event' from validated_data

        event_user = EventUserModel.objects.create(event_picker=event_picker, **validated_data)

        for event in events_data:
            event_user.event.add(event)  # Add each event to the many-to-many relationship

        return event_user