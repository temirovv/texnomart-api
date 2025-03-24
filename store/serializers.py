from rest_framework import serializers
from .models import Promotion, Category, Product


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'image', 'title', 'description', 'is_active', 'start', 'end']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'installment_payment_12', 'installment_payment_24', 'attributes']
