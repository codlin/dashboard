from django.db import models
import djongo.models

# <product id>
# CRT product data, e.g.:
# fzmfdd: 'FZM FDD'
# cfzcfdd: 'CFZC TDD'


class Product(models.Model):
    name = models.CharField('Product Name', max_length=16)
    text = models.CharField('Product Text', max_length=16)

    class Meta:
        db_table = "crt_product"

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

#------------------testline table-----------------------#
# <testline>


class Testline(models.Model):
    mode = models.CharField('Mode', max_length=8)
    sitetype = models.CharField('Site Type', max_length=16)
    node = models.CharField('Jenkins Node', max_length=64)
    btsid = models.CharField('BTSID', max_length=8, primary_key=True)
    ca = models.CharField('CA', max_length=64)
    jenkinsjob = models.CharField('Jenkins Job', max_length=255)
    mbtsid = models.CharField('Mobility BTSID', max_length=8)
    mnode = models.CharField('Mobility Node', max_length=64)

    class Meta:
        db_table = "crt_testline"

    def __str__(self):
        return str(self.btsid)

#------------------case-related table-----------------------#
# <case path>


class TesecasePath(models.Model):
    path = models.CharField('Case path', max_length=255)

    class Meta:
        db_table = "crt_testcasepath"

    def __str__(self):
        return self.path

# <testcase>


class Testcase(models.Model):
    casename = models.CharField('Case name', max_length=255)
    path = models.ForeignKey(TesecasePath, on_delete=models.CASCADE)

    class Meta:
        db_table = "crt_testcase"

    def __str__(self):
        return self.casename

# <release -- testcase>


class TestcaseRelease(models.Model):
    release = models.CharField('Release', max_length=16)
    case = models.ForeignKey(Testcase, on_delete=models.CASCADE)

    class Meta:
        db_table = "crt_testcase_release"

    def __str__(self):
        return self.release

# <load--testcase--testline> scheduler


class LoadTestcaseSchedule(models.Model):
    loadname = models.CharField('Load Name', max_length=64)
    case = models.ForeignKey(Testcase, on_delete=models.DO_NOTHING)
    btsid = models.CharField('BTSID', max_length=8)

    class Meta:
        db_table = "crt_load_testcase_schedule"

    def __str__(self):
        return "{}_{}_{}".format(self.loadname, self.btsid, self.case)

#------------------run history table-----------------------#
# <load--testcase status>


class LoadTestcaseStatus(models.Model):
    loadname = models.CharField('Load name', max_length=64)
    casename = models.CharField('Case name', max_length=255)
    btsid = models.CharField('BTSID', max_length=8)
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
    btsid = models.CharField('BTSID', max_length=8)
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
        return self.loadname
