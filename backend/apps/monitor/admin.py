from django.contrib import admin

from .models import LoadStatus, Product, SysMenu

# Register your models here.
admin.site.register(LoadStatus)
admin.site.register(Product)
admin.site.register(SysMenu)
