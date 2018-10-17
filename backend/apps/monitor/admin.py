# pylint: disable=W0614
from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(SysMenu)
admin.site.register(Testline)
admin.site.register(CaseName)
admin.site.register(CasePath)
admin.site.register(TestcaseRelease)
admin.site.register(LoadTestcaseStatus)
admin.site.register(LoadTestlineStatus)
admin.site.register(LoadStatus)
admin.site.register(JenkinsInfo)
admin.site.register(JenkinsJobs)
admin.site.register(JenkinsJobMonitor)
admin.site.register(CaseSchedule)
admin.site.register(TestlineStableLoad)
