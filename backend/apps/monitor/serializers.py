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


class LoadTestlineStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadTestlineStatus
        fields = ('loadname', 'testline', 'btsid', 'ca',
                  'checksite_time', 'checksite_status', 'checksite_url',
                  'healthcheck_time', 'healthcheck_status', 'healthcheck_url',
                  'upgrade_time', 'upgrade_status', 'upgrade_url')


class LoadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadStatus
        fields = "__all__"
