from rest_framework import serializers
from .models import Event, EventImage
from location.models import Location
from django.contrib.auth.models import User

class EventImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = EventImage
        fields = ['id', 'image_url','b_preview']

    def get_image_url(self,obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None
    def get_b_preview(self,obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.b_preview) if request else obj.b_preview
        return None

class EventLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','name','coordinateX','coordinateY']

class EventAuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','username','full_name']
    def get_full_name(self, obj):
        full_name = (obj.first_name + " "+ obj.last_name).strip() 
        return full_name if full_name else obj.username

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    id_location= EventLocationSerializer(many=False, read_only=True)
    author = EventAuthorSerializer(many=False, read_only=True)
    class Meta:
        model = Event
        fields = ['id','name','description','start_date','end_date','author','top','pub_date','status','images','id_location'] 