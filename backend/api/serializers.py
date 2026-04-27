from rest_framework import serializers
from .models import Crop, Scheme, Buyer, CropPriceHistory

class CropPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CropPriceHistory
        fields = ['price', 'date']

class CropSerializer(serializers.ModelSerializer):
    price_history = CropPriceHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Crop
        fields = '__all__'

class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme
        fields = '__all__'

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
