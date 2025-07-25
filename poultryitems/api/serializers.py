# items/api/serializers.py

from rest_framework import serializers
from poultryitems.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
