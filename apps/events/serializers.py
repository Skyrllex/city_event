from rest_framework import serializers
from .models import Event, EventImage

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


class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = ['id','name','description','start_date','end_date','author','top','pub_date','status','images'] 