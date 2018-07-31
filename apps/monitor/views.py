from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import LoadStatus
from .serializers import LoadStatusSerializer

# Create your views here.
# class LoadPipelineList(APIView):
#     def get(self, request, format=None):
#         pipeline = LoadPipeline.objects.all()
#         serializer = LoadPipelineSerializer(pipeline, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = LoadPipelineSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         loadname = serializer.get_fields().get('load_name')
#         rootbuildnum = serializer.get_fields().get('root_buildnum')
#         item = LoadPipeline.objects.filter(
#             load_name=loadname, root_buildnum=rootbuildnum)
#         if item:
#             serializer.update(item, request.data)
#         else:
#             serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)

loadStatusFilter = {
    'fzmfdd': 'FLF',
    'fzmtdd': 'TLF',
    'cfzcfdd': 'FLC',
    'cfzctdd': 'TLC'
}

class LoadStatusView(viewsets.ModelViewSet):
    serializer_class = LoadStatusSerializer
    def get_queryset(self):
        productid = self.request.query_params.get('productid', default='fzmfdd')
        load_prefix = loadStatusFilter.get(productid, None)
        if load_prefix is None:
            Response(status=status.HTTP_400_BAD_REQUEST)

        print(load_prefix)
        Loads = LoadStatus.objects.filter(
            load_name__startswith=load_prefix).order_by('-start_time')[:50]
        
        print(Loads)

        # get load info, if exist, execute incremental update
        loadFrom = self.request.query_params.get('from', default=None)
        if loadFrom:
            Loads = Loads.filter(start_time__gte=loadFrom.starttime)
        
        return Loads

