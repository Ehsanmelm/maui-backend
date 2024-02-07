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

        event = EventModel.objects.create(event_maker=event_maker , **validated_data)
        event.save()

        return event
    
class EventUserSerializer(serializers.ModelSerializer):
    event_picker = serializers.CharField(read_only =True)
    class Meta:
        model = EventUserModel
        fields = '__all__'
    

    def create(self, validated_data):
        event_picker = UserModel.objects.get(id=self.context['id'])
        events_data = validated_data.pop('event', [])  # Remove 'event' from validated_data

        event_user , is_created = EventUserModel.objects.get_or_create(event_picker=event_picker, **validated_data)

        for event in events_data:

            selected_event = EventModel.objects.get(id= event.id)

            if selected_event in event_user.event.all():
                raise serializers.ValidationError("this event is in you selected event")
            
            else:
                if selected_event.capacity > 0:

                    selected_event.capacity -= 1
                    selected_event.save()
                    event_user.event.add(event)  # Add each event to the many-to-many relationship

                else:
                    raise serializers.ValidationError('event is full')
            
        return event_user