from rest_framework import serializers
from api.models import YieldHabit

class YieldHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldHabit
        fields = ['scale', 'created_on', 'edited_on'] 