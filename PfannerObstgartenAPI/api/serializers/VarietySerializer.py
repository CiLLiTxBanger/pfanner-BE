from rest_framework import serializers
from api.models import Variety, Image
from api.serializers.ImageSerializer import ImageSerializer


class VarietySerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Variety
        fields = ['id', 'name', 'image', 'blossom', 'fruit', 'climate', 'pick_maturity', 'usage', 'pollinator', 'properties', 'output', 'disease_possibility', 'description',  'created_on', 'edited_on']

    def create(self, validated_data):
        image = validated_data.pop['image']
        variety = Variety.objects.create(**validated_data)

        Image.objects.create(**image, variety=variety)

        return variety
        #depth = 1

#    def create(self, validated_data):
#        images_data = validated_data.pop('image')
#        image_model = Image.objects.create(**images_data)

#        variety = Variety.objects.create(image=image_model, **validated_data)
#        return variety
    
class WriteVarietySerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Variety
        fields = ['id', 'name', 'image', 'blossom', 'fruit', 'climate', 'pick_maturity', 'usage', 'pollinator', 'properties', 'output', 'disease_possibility', 'description',  'created_on', 'edited_on']

    def create(self, validated_data):
        image = validated_data.pop("image", None)
        return super().create(validated_data)