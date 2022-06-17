from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Tree
from api.serializers.VarietySerializer import VarietySerializer

class TreeSerializer(serializers.ModelSerializer):
    variety = VarietySerializer()

    class Meta:
        model = Tree
        fields = ['id', 'type', 'variety', 'row', 'column', 'planted_on', 'location', 'organic', 'latitude', 'longitude', 'cut', 'active', 'created_on', 'edited_on']

class WriteTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['id', 'type', 'variety', 'row', 'column', 'planted_on', 'location', 'organic', 'latitude', 'longitude', 'cut', 'active', 'created_on', 'edited_on']