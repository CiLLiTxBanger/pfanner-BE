from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Tree

class UserSerializer(serializers.HyperlinkedModelSerializer):
    trees = serializers.HyperlinkedRelatedField(many=True, view_name='tree-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'trees']