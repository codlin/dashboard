from django.contrib import admin

from .models import Product, SysMenu, Testline, TesecasePath, Testcase, TestcaseRelease, LoadTestcaseSchedule, LoadTestcaseStatus, LoadTestlineStatus, LoadStatus

# Register your models here.
admin.site.register(Product)
admin.site.register(SysMenu)
admin.site.register(Testline)
admin.site.register(TesecasePath)
admin.site.register(Testcase)
admin.site.register(TestcaseRelease)
admin.site.register(LoadTestcaseSchedule)
admin.site.register(LoadTestcaseStatus)
admin.site.register(LoadTestlineStatus)
admin.site.register(LoadStatus)
