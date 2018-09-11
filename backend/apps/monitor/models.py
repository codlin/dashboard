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
    load_release = models.CharField('Release', max_length=16)
    case = models.ForeignKey(Testcase, on_delete=models.CASCADE)

    class Meta:
        db_table = "crt_testcase_release"

    def __str__(self):
        return self.load_release

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


class JenkinsJobs(models.Model):
    job = models.CharField('Jenkins Job', max_length=255, unique=True)

    class Meta:
        db_table = "crt_jenkins_job"

    def __str__(self):
        return self.job


class JenkinsInfo(models.Model):
    url = models.CharField('Jenkins URL', max_length=128, unique=True)
    user = models.CharField('Jenkins User', max_length=16)
    passwd = models.CharField('Jenkins Password', max_length=16)

    jobs = models.ManyToManyField(JenkinsJobs, through='JenkinsJobMonitor')

    class Meta:
        db_table = "crt_jenkins_info"

    def __str__(self):
        return self.url


class JenkinsJobMonitor(models.Model):
    jenkins = models.ForeignKey(JenkinsInfo, on_delete=models.CASCADE)
    jobs = models.ForeignKey(JenkinsJobs, on_delete=models.CASCADE)
    product = models.CharField('Product', max_length=8)

    class Meta:
        db_table = "crt_jenkins_monitor"

    def __str__(self):
        return "{}_{}_{}".format(self.product, self.jenkins, self.jobs)

# <load--testline status>


class LoadTestlineStatus(models.Model):
    loadname = models.CharField('Load name', max_length=64)
    testline = models.CharField('Testline', max_length=64)
    btsid = models.CharField('BTSID', max_length=8)
    ca = models.CharField('CA', max_length=64)

    jenkins = models.ForeignKey(JenkinsInfo, on_delete=models.DO_NOTHING)

    checksite_name = models.ForeignKey(
        JenkinsJobs, related_name='job_checksite', on_delete=models.DO_NOTHING)
    checksite_buildid = models.CharField('Checksite Build ID', max_length=8)
    checksite_time = models.CharField('Checksite Time', max_length=32)
    checksite_status = models.CharField(
        'Checksite Status', max_length=8, null=True, blank=True)
    checksite_url = models.CharField('Checksite URL', max_length=512)

    # FZC no these colums
    healthcheck_name = models.ForeignKey(
        JenkinsJobs, related_name='job_healthcheck', on_delete=models.DO_NOTHING, blank=True)
    healthcheck_buildid = models.CharField(
        'Healthcheck Build ID', max_length=8, null=True, blank=True)
    healthcheck_time = models.CharField(
        'Healthcheck Time', max_length=32, null=True, blank=True)
    healthcheck_status = models.CharField(
        'Healthcheck Status', max_length=8, null=True, blank=True)
    healthcheck_url = models.CharField(
        'Healthcheck URL', max_length=512, null=True, blank=True)

    upgrade_name = models.ForeignKey(
        JenkinsJobs, related_name='job_upgrade', on_delete=models.DO_NOTHING)
    upgrade_buildid = models.CharField('Upgrade Build ID', max_length=8)
    upgrade_time = models.CharField(
        'Upgrade Time', max_length=32, null=True, blank=True)
    upgrade_status = models.CharField(
        'Upgrade Status', max_length=8, null=True, blank=True)
    upgrade_url = models.CharField('Upgrade URL', max_length=512)

    class Meta:
        db_table = "crt_load_testline_status_page"

    def __str__(self):
        return "{}_{}".format(self.loadname, self.btsid)

# <load> status


class LoadStatus(models.Model):
    start_time = models.CharField('Start Time', max_length=32)
    loadname = models.CharField('Load', max_length=32, unique=True)
    passed_num = models.CharField('Passed', max_length=8)
    failed_num = models.CharField('Failed', max_length=8)
    norun_num = models.CharField('NA', max_length=8)
    total_num = models.CharField('Total', max_length=8)
    first_passrate = models.CharField('First PassRate', max_length=8)
    passrate = models.CharField('PassRate', max_length=8)
    debug = models.CharField('Debug', max_length=8)

    class Meta:
        db_table = "crt_loadstatus_page"

    def __str__(self):
        return self.loadname
