from rest_framework import serializers
from .models import Product, SysMenu, Testline, TesecasePath, Testcase, TestcaseRelease, LoadTestcaseSchedule, LoadTestcaseStatus, LoadTestlineStatus, LoadStatus


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


class TesecasePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesecasePath
        fields = "__all__"


class TestcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testcase
        fields = "__all__"


class TestcaseReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestcaseRelease
        fields = "__all__"


class LoadTestcaseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadTestcaseSchedule
        fields = "__all__"


class LoadTestcaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysMenu
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
