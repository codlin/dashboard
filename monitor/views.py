from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import LoadJobStatus, LoadPipeline
from .serializers import LoadJobStatusSerializer, LoadPipelineSerializer

# Create your views here.
class IndexView(generic.View):
    template_name = 'monitor/index.html'
    context_object_name = 'latest_jobstatus_table'

    def get_queryset(self):
        latest_jobstatus = LoadJobStatus.objects.order_by('-timestamp')[:5]
        

def loadpipeline_list(request):
    if request.method == 'GET':
        pipeline = LoadPipeline.objects.all()
        serializer = LoadPipelineSerializer(pipeline, many=True)
        return JsonResponse(serializer.data, safe=False)
    