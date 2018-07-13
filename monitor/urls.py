from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /monitor/
    url(r'^monitor/$', views.loadpipeline_list),
]