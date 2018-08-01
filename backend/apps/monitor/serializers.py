from rest_framework import serializers
from .models import LoadStatus

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

class LoadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadStatus
        fields="__all__"