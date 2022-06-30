from rest_framework import serializers
from api.models import Variety


class VarietySerializer(serializers.ModelSerializer):

    class Meta:
        model = Variety
        fields = ['id', 'name', 'image_photo', 'image_description', 'blossom', 'climate', 'pick_maturity', 'usage', 'pollinator', 'properties', 'output', 'disease_possibility', 'description',  'created_on', 'edited_on']
