from rest_framework import serializers
from .models import Category, SubCategory, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'title'
        ]
        model = Category

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'category',
            'title1'
        ]
        model = SubCategory


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'item_tag',
            'name',
            'category',
            'subcategory',
            'price',
            'units'
        ]
        model = Item



