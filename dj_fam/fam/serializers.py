from rest_framework import serializers
from .models import Human


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"

    def create(self):
        return Human(name=self.validated_data['name'], age=self.validated_data['age'],
                     height=self.validated_data['height'], weight=self.validated_data['weight'],
                     occupation=self.validated_data['occupation'])
"""
class HumanSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time = serializers.DateTimeField()
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField(max_value=120, min_value=0)  # years
    height = serializers.IntegerField(max_value=300, min_value=1)  # cm
    weight = serializers.IntegerField(max_value=999, min_value=1)  # kg
    occupation = serializers.CharField(max_length=50)
"""



