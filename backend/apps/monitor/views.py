from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Product, SysMenu, Testline, TesecasePath, Testcase, TestcaseRelease, LoadTestcaseSchedule, LoadTestcaseStatus, LoadTestlineStatus, LoadStatus
from .serializers import ProductSerializer, SysMenuSerializer, TestlineSerializer, TesecasePathSerializer, TestcaseSerializer, TestcaseReleaseSerializer, LoadTestcaseScheduleSerializer, LoadTestcaseStatusSerializer, LoadTestlineStatusSerializer, LoadStatusSerializer

# Create your views here.


class ProductApi(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class SysMenuApi(viewsets.ModelViewSet):
    serializer_class = SysMenuSerializer

    def get_queryset(self):
        return SysMenu.objects.all()


loadStatusFilter = {
    'fzmfdd': 'FLF',
    'fzmtdd': 'TLF',
    'cfzcfdd': 'FLC',
    'cfzctdd': 'TLC'
}


class LoadStatusViewApi(viewsets.ModelViewSet):
    serializer_class = LoadStatusSerializer

    def get_queryset(self):
        productid = self.request.query_params.get('productid')
        load_prefix = loadStatusFilter.get(productid, None)
        if load_prefix is None:
            return LoadStatus.objects.filter(start_time__lte='1900-01-1 00:00:00Z')

        Loads = LoadStatus.objects.filter(
            load_name__startswith=load_prefix).order_by('-start_time')

        # get load info, if exist, execute incremental update
        loadFrom = self.request.query_params.get('from', default=None)
        if loadFrom:
            Loads = Loads.filter(start_time__gt=loadFrom)

        return Loads
