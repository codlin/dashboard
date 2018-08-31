from rest_framework import serializers
from .models import LoadStatus, Product, SysMenu


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SysMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysMenu
        fields = "__all__"


class LoadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadStatus
        fields = "__all__"
