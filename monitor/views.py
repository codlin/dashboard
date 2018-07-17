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
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LoadPipelineSerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
        
        loadname = serializer.get_fields().get('load_name')
        rootbuildnum = serializer.get_fields().get('root_buildnum')
        item = LoadPipeline.objects.filter(load_name=loadname, root_buildnum=rootbuildnum)
        if item:
            serializer.update(item, data)
        else:
            serializer.save()
        
        return JsonResponse(serializer.data, status=201)
        