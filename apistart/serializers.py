from rest_framework import serializers
from .models import Pantry
from .models import Basket
class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'