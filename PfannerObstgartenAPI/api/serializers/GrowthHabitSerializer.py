from rest_framework import serializers
from api.models import GrowthHabit

class GrowthHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthHabit
        fields = ['id', 'scale', 'created_on', 'edited_on'] 