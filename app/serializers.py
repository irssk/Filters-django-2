from rest_framework import serializers
from app import models


class SerializedMenuItem(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = '__all__'


class SerializedCategory(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'