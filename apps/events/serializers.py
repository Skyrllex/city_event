from rest_framework import serializers
from .models import Event, EventImage

class EventImageSeirializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()


    class Meta:
        model = EventImage
        fields = ['id', 'image']



class EventSerializer(serializers.ModelSerializer):
    images = EventImageSeirializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = ['name','start_date','end_date','images','status'] 