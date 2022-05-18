from rest_framework import serializers
from api.models import Image

class ImageSerializer(serializers.ModelSerializer):

    photo = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'photo', 'variety', 'orchardMeasurement', 'created_on', 'edited_on']