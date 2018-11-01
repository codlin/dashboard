"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from apps.monitor.views import LoadStatusViewApi, ProductApi, ProductReleaseApi, SysMenuApi, TestlineViewApi, LoadTestcaseStatusViewApi, LoadTestlineStatusViewApi

router = DefaultRouter()

router.register(r'menu', SysMenuApi, base_name="menu")
router.register(r'products', ProductApi, base_name="products")
router.register(r'productrelease', ProductReleaseApi,
                base_name="productrelease")
router.register(r'loads', LoadStatusViewApi, base_name="loads")
router.register(r'loadcases', LoadTestcaseStatusViewApi, base_name="loadcases")
router.register(r'loadtls', LoadTestlineStatusViewApi, base_name="loadtls")
router.register(r'testlines', TestlineViewApi, base_name="testlines")

urlpatterns = [
    path('admin/', admin.site.urls),

    # jwt的认证接口
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    # router的path路径
    re_path('^api/', include(router.urls)),
    # re_path('^api/loadtls/', LoadTestlineStatusViewApi.as_view()),

    # url(r'^', TemplateView.as_view(template_name="index.html")),
]
