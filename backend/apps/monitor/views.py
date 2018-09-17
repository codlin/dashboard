# pylint: disable=E1101
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Product, SysMenu, Testline, CaseName, CasePath, TestcaseRelease, LoadTestcaseStatus, LoadTestlineStatus, LoadStatus
from .serializers import ProductSerializer, SysMenuSerializer, TestlineSerializer, CaseNameSerializer, CasePathSerializer, TestcaseReleaseSerializer, LoadTestcaseStatusSerializer, LoadTestlineStatusSerializer, LoadStatusSerializer


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
            return LoadStatus.objects.all().order_by('-start_time')

        Loads = LoadStatus.objects.filter(
            loadname__startswith=load_prefix).order_by('-start_time')

        # get load info, if exist, execute incremental update
        loadFrom = self.request.query_params.get('from', default=None)
        if loadFrom:
            Loads = Loads.filter(start_time__gt=loadFrom)

        return Loads


class LoadTestcaseStatusViewApi(viewsets.ModelViewSet):
    serializer_class = LoadTestcaseStatusSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        items = LoadTestcaseStatus.objects.filter(
            loadname=name).order_by('casename')

        return items


class LoadTestlineStatusViewApi(viewsets.ModelViewSet):
    serializer_class = LoadTestlineStatusSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        items = LoadTestlineStatus.objects.filter(
            loadname=name).order_by('testline')

        return items


class TestlineViewApi(viewsets.ModelViewSet):
    serializer_class = TestlineSerializer

    def get_queryset(self):
        return Testline.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
