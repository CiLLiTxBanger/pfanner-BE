from rest_framework import serializers
from api.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'image', 'tree', 'orchardMeasurement', 'created_on', 'edited_on'] 