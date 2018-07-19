from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import LoadJobStatus, LoadPipeline
from .serializers import LoadJobStatusSerializer, LoadPipelineSerializer

# Create your views here.


class LoadPipelineList(APIView):
    def get(self, request,  format=None):
        pipeline = LoadPipeline.objects.all()
        serializer = LoadPipelineSerializer(pipeline, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoadPipelineSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        loadname = serializer.get_fields().get('load_name')
        rootbuildnum = serializer.get_fields().get('root_buildnum')
        item = LoadPipeline.objects.filter(
            load_name=loadname, root_buildnum=rootbuildnum)
        if item:
            serializer.update(item, request.data)
        else:
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
