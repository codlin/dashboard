from django.db import models
import djongo.models

# <testcase>
class Testcase(models.Model):
    caseid = models.PositiveSmallIntegerField('Case ID', primary_key=True)
    casename = models.CharField('Case name', max_length=255)
    path = models.CharField('Case path', max_length=255)

    class Meta:
        db_table = "crt_testcase"

    def __str__(self):
        return self.casename

# <load--testcase--testline> scheduler
class LoadTestcaseSchedule(models.Model):
    loadname = models.CharField('Load Name', max_length=64)
    caseid = models.ForeignKey(Testcase, on_delete=models.DO_NOTHING)
    btsid = models.PositiveIntegerField('BTSID')

    class Meta:
        db_table = "crt_load_testcase_schedule"

    def __str__(self):
        return "{}_{}_{}".format(self.loadname, self.btsid, self.caseid)

# <load--testcase status> 
class LoadTestcaseStatus(models.Model):
    loadname = models.CharField('Load name', max_length=64)
    casename = models.CharField('Case name', max_length=255)
    btsid = models.PositiveIntegerField('BTSID')
    node = models.CharField('Jenkins Node', max_length=64)
    result = models.CharField('Result', max_length=64)
    suite = models.CharField('Suite', max_length=64)

    class Meta:
        db_table = "crt_load_testcase_status_page"

    def __str__(self):
        return "{}_{}".format(self.loadname, self.casename)

# <load--testline status>
class LoadTestlineStatus(models.Model):
    loadname = models.CharField('Load name', max_length=64)
    testline = models.CharField('Testline', max_length=255)
    btsid = models.PositiveIntegerField('BTSID')
    ca = models.CharField('CA', max_length=64)

    checksite_time = models.DateTimeField('Checksite Time')
    checksite_status = models.CharField('Checksite Status', max_length=8)
    checksite_url = models.CharField('Checksite URL', max_length=512)

    healthcheck_time = models.DateTimeField('Healthcheck Time')
    healthcheck_status = models.CharField('Healthcheck Status', max_length=8)
    healthcheck_url = models.CharField('Healthcheck URL', max_length=512)

    upgrade_time = models.DateTimeField('Upgrade Time')
    upgrade_status = models.CharField('Upgrade Status', max_length=8)
    upgrade_url = models.CharField('Upgrade URL', max_length=512)

    class Meta:
        db_table = "crt_load_testline_status_page"

    def __str__(self):
        return "{}_{}".format(self.loadname, self.btsid)

# <load> status
class LoadStatus(models.Model):
    start_time = models.DateTimeField('Start Time')
    loadname = models.CharField('Load', max_length=30)
    passed_num = models.PositiveIntegerField('Passed')
    failed_num = models.PositiveIntegerField('Failed')
    norun_num = models.PositiveIntegerField('NA')
    total_num = models.PositiveIntegerField('Total')
    first_passrate = models.FloatField('First PassRate')
    passrate = models.FloatField('PassRate')

    class Meta:
        db_table = "crt_loadstatus_page"

    def __str__(self):
        return "{}_{}".format(self.loadname, self.passrate)

# <product id>
# CRT product data, e.g.:
# fzmfdd: 'FZM FDD'
# cfzcfdd: 'CFZC TDD'
class Product(models.Model):
    name = models.CharField('Product Name', max_length=16)
    text = models.CharField('Product Text', max_length=16)

    class Meta:
        db_table = "crt_product_page"

    def __str__(self):
        return self.name

# <system menu>
class SysMenu(models.Model):
    index = models.PositiveSmallIntegerField('Index')
    level = models.PositiveSmallIntegerField('Level')
    group = models.CharField('Group', max_length=8)
    name = models.CharField('Name', max_length=16)
    text = models.CharField('Text', max_length=16)

    class Meta:
        db_table = "crt_sysmenu_page"

    def __str__(self):
        return self.name

# <release -- testcase>
class TestcaseRelease(models.Model):
    release = models.CharField('Release', max_length=16)
    caseid = models.ForeignKey(Testcase, on_delete=models.CASCADE)

    class Meta:
        db_table = "crt_testcase_release"

    def __str__(self):
        return "{}_{}".format(self.release, self.caseid)

# <testline>
class Testline(models.Model):
    mode = models.CharField('Mode', max_length=8)
    sitetype = models.CharField('Site Type', max_length=16)
    node = models.CharField('Jenkins Node', max_length=64)
    btsid = models.PositiveSmallIntegerField('BTS ID', primary_key=True)
    ca = models.CharField('CA', max_length=64)
    jenkinsjob = models.CharField('Jenkins Job', max_length=255)
    mbtsid = models.PositiveSmallIntegerField('Mobility BTSID')
    mnode = models.CharField('Mobility Node', max_length=64)

    class Meta:
        db_table = "crt_testline"

    def __str__(self):
        return self.btsid
