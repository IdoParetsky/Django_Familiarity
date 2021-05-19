from rest_framework import serializers
from .models import Human

"""
class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"
"""


class HumanSerializer(serializers.Serializer):
    #id = serializers.IntegerField()
    #time = serializers.DateTimeField()
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField(max_value=120, min_value=0)  # years
    height = serializers.IntegerField(max_value=300, min_value=1)  # cm
    weight = serializers.IntegerField(max_value=999, min_value=1)  # kg
    occupation = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Human(validated_data)
