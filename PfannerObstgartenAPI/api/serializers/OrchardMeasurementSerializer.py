from rest_framework import serializers
from api.models import OrchardMeasurement, Image
from api.serializers import *

class OrchardMeasurementSerializer(serializers.ModelSerializer):
    #image = ImageSerializer()
    class Meta:
        model = OrchardMeasurement
        fields = ['id', 'description', 'tree', 'image_photo', 'image_description', 'frostSensitivity', 'growthHabit', 'yieldHabit', 'season', 'temperature', 'precipitation', 'lateFrost', 'status', 'created_on', 'edited_on']

    #def create(self, validated_data):
        #image_data = validated_data.pop('image')
        #image = Image.objects.create(**image_data)
        #orchardMeasurement = OrchardMeasurement.objects.create(image=image, **validated_data)

        #return orchardMeasurement