# pylint: disable=E1101
import logging
import json
from django.db import connection
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status

from .models import Product, ProductRelease, SysMenu, Testline, CaseName, CasePath, TestcaseRelease, LoadTestcaseStatus, LoadTestlineStatus, LoadStatus
from .serializers import ProductSerializer, ProductReleaseSerializer, SysMenuSerializer, TestlineSerializer, CaseNameSerializer, CasePathSerializer, TestcaseReleaseSerializer, LoadTestcaseStatusSerializer, LoadTestlineStatusSerializer, LoadStatusSerializer


# Create your views here.


class ProductApi(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class ProductReleaseApi(viewsets.ModelViewSet):
    serializer_class = ProductReleaseSerializer

    def get_queryset(self):
        return ProductRelease.objects.all()


class SysMenuApi(viewsets.ModelViewSet):
    serializer_class = SysMenuSerializer

    def get_queryset(self):
        return SysMenu.objects.all()


loadStatusFilter = {
    'fzmfdd': 'FLF',
    'fzmtdd': 'TLF',
    'cfzcfdd': 'FLC',
    'cfzctdd': 'TLC',
    'asirfdd': 'FL',
    'asirtdd': 'TL'
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


class LoadTestlineStatusViewApi(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    # serializer_class = LoadTestlineStatusSerializer

    def list(self, request):
        name = request.query_params.get('name')
        query_sql = "SELECT id, loadname, testline, t.cfgid, url, GROUP_CONCAT(CONCAT_WS(',', job, build_status, build_time, build_url)  ORDER BY t.order SEPARATOR ';' ) as jobs \
                     FROM (SELECT a.id, loadname, testline, c.cfgid, url, a.job, build_status, build_time, build_url, b.order \
                            FROM crt_db.crt_load_testline_status_page a \
                            LEFT JOIN crt_db.crt_jenkins_job b ON a.job = b.job \
                            INNER JOIN crt_db.crt_testline c ON a.testline = c.node \
                            WHERE loadname = '{}') t \
                     GROUP BY loadname, testline ORDER BY loadname, testline;".format(name)

        items = None
        with connection.cursor() as cursor:
            cursor.execute(query_sql)
            row_headers = [x[0] for x in cursor.description]
            items = cursor.fetchall()
            # logging.error(row_headers)
            json_data = []
            for item in items:
                data = dict(zip(row_headers, item))
                # logging.error(data)
                json_data.append(data)

            return Response(json_data)


class TestlineViewApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    serializer_class = TestlineSerializer

    def get_queryset(self):
        return Testline.objects.all()

    def create(self, request):
        return super().create(request)

    def update(self, request, pk=None):
        logging.info("pk: {}".format(pk))
        return super().update(request, pk)

    def destroy(self, request, pk=None):
        logging.info("pk: {}".format(pk))
        return super().destroy(request, pk)
