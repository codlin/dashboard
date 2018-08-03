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
        fields="__all__"

# class LoadJobStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LoadJobStatus
#         fields = ('job_name', 'build_num', 'node_name', 'build_result',
#                   'timestamp')

# class LoadPipelineSerializer(serializers.ModelSerializer):
#     jobs = LoadJobStatusSerializer(many=True, read_only=True)

#     class Meta:
#         model = LoadPipeline
#         fields = ('load_name', 'root_buildnum', 'jobs')
