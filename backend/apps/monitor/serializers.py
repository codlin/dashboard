from rest_framework import serializers
from .models import Product, SysMenu, Testline, CaseName, CasePath, TestcaseRelease, LoadTestcaseStatus, LoadTestlineStatus, LoadStatus


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SysMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysMenu
        fields = "__all__"


class TestlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testline
        fields = "__all__"


class CasePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasePath
        fields = "__all__"


class CaseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseName
        fields = "__all__"


class TestcaseReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestcaseRelease
        fields = "__all__"


class LoadTestcaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadTestcaseStatus
        fields = "__all__"


# class LoadTestlineStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LoadTestlineStatus
#         fields = "__all__"

class LoadTestlineStatusSerializer(serializers.Serializer):
    loadname = serializers.CharField(max_length=64)
    testline = serializers.CharField(max_length=64)
    btsid = serializers.CharField(max_length=8)
    url = serializers.CharField(max_length=128)
    jobs = serializers.CharField(max_length=1024)


class LoadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadStatus
        fields = "__all__"
