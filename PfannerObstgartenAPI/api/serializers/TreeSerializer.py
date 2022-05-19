from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Tree, Variety, Location

class TreeSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tree
        fields = ['url', 'id', 'type', 'variety', 'row', 'column', 'planted_on', 'location', 'organic', 'latitude', 'longitude', 'cut', 'active', 'owner', 'created_on', 'edited_on']
        #read_only_fields = ['url', 'owner'] 
        
        depth = 0