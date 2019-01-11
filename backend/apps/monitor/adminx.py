# pylint: disable=W0614
import xadmin
from xadmin import views

from .models import *


class GlobalSetting(object):
    site_title = 'CRT Dashboard'
    site_footer = 'CRT Dashboard'
    # menu_style = 'accordion'


class ProductAdmin(object):
    list_display = ['id', 'name', 'text']  # columes will display
    search_fields = ['name', 'text']  # columes want to be searched
    list_filter = ['name', 'text']  # columes want to be filtered


class ProductReleaseAdmin(object):
    list_display = ['id', 'product',
                    'release']  # columes will display
    search_fields = ['product__name', 'release']  # columes want to be searched
    list_filter = ['product', 'release']  # columes want to be filtered


class CaseNameAdmin(object):
    list_display = ['id', 'casename']  # columes will display
    search_fields = ['casename']  # columes want to be searched
    list_filter = ['casename']  # columes want to be filtered


class CasePathAdmin(object):
    list_display = ['id', 'casepath']  # columes will display
    search_fields = ['casepath']  # columes want to be searched
    list_filter = ['casepath']  # columes want to be filtered


class TestcaseReleaseAdmin(object):
    list_display = ['id', 'release', 'case', 'path']  # columes will display
    search_fields = ['release__release', 'case__casename',
                     'path__casepath']  # columes want to be searched
    list_filter = ['release', 'case', 'path']  # columes want to be filtered


class CaseScheduleAdmin(object):
    list_display = ['id', 'testline', 'case', ]  # columes will display
    # columes want to be searched
    search_fields = ['testline__node', 'testline__cfgid',
                     'testline__mnode', 'testline__mbtsid',  'case__casename']
    list_filter = ['testline', 'case']  # columes want to be filtered


# Register your models here.
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(ProductRelease, ProductReleaseAdmin)
xadmin.site.register(CaseName, CaseNameAdmin)
xadmin.site.register(CasePath, CasePathAdmin)
xadmin.site.register(TestcaseRelease, TestcaseReleaseAdmin)
xadmin.site.register(CaseSchedule, CaseScheduleAdmin)
