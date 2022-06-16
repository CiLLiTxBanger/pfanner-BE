from rest_framework import serializers
from api.models import Variety, Image
from api.serializers.ImageSerializer import ImageSerializer


class VarietySerializer(serializers.ModelSerializer):

    class Meta:
        model = Variety
        fields = ['id', 'name', 'image_photo', 'image_description', 'blossom', 'fruit', 'climate', 'pick_maturity', 'usage', 'pollinator', 'properties', 'output', 'disease_possibility', 'description',  'created_on', 'edited_on']

    #def create(self, validated_data):
        #image_data = validated_data.pop('image')
        #image = Image.objects.create(**image_data)
        #variety = Variety.objects.create(image=image, **validated_data)

        #return variety