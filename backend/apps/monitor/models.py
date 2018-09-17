from django.db import models
import djongo.models


class Product(models.Model):
    '''
    CRT product data, e.g.:
    fzmfdd: 'FZM FDD'
    cfzcfdd: 'CFZC TDD'
    '''
    name = models.CharField('Product Name', max_length=16, default="")
    text = models.CharField('Product Text', max_length=16, default="")

    class Meta:
        db_table = "crt_product"

    def __str__(self):
        return self.name


class SysMenu(models.Model):
    index = models.PositiveSmallIntegerField('Index', default=0)
    level = models.PositiveSmallIntegerField('Level', default=0)
    group = models.CharField('Group', max_length=8, default="")
    name = models.CharField('Name', max_length=16, default="")
    text = models.CharField('Text', max_length=16, default="")

    class Meta:
        db_table = "crt_sysmenu_page"

    def __str__(self):
        return self.name


class Testline(models.Model):
    mode = models.CharField('Mode', max_length=8, default="")
    sitetype = models.CharField('Site Type', max_length=16, default="")
    node = models.CharField('Jenkins Node', max_length=64, default="")
    btsid = models.CharField('BTSID', max_length=8,
                             primary_key=True, default="")
    ca = models.CharField('CA', max_length=64, default="")
    jenkinsjob = models.CharField('Jenkins Job', max_length=255, default="")
    mbtsid = models.CharField('Mobility BTSID', max_length=8, default="NA")
    mnode = models.CharField('Mobility Node', max_length=64, default="NA")

    class Meta:
        db_table = "crt_testline"

    def __str__(self):
        return "{}_{}_{}_{}_{}_{}_{}_{}".format(self.mode, self.sitetype, self.node, self.btsid,
                                                self.ca, self.jenkinsjob, self.mbtsid, self.mnode)


class CasePath(models.Model):
    casepath = models.CharField('Case path', max_length=255,
                                unique=True, default="")

    class Meta:
        db_table = "crt_casepath"

    def __str__(self):
        return self.casepath


class CaseName(models.Model):
    casename = models.CharField(
        'Case name', max_length=255, unique=True, default="")

    class Meta:
        db_table = "crt_casename"

    def __str__(self):
        return self.casename


class TestcaseRelease(models.Model):
    load_release = models.CharField(
        'Release', max_length=16, default="")
    case = models.ForeignKey(CaseName, on_delete=models.CASCADE, default="")
    path = models.ForeignKey(CasePath, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = "crt_testcase_release"
        unique_together = (("load_release", "case", "path"),)

    def __str__(self):
        return "{}_{}_{}".format(self.load_release, self.case, self.path)


class LoadTestcaseStatus(models.Model):
    loadname = models.CharField('Load name', max_length=64, default="")
    casename = models.CharField('Case name', max_length=255, default="")
    btsid = models.CharField('BTSID', max_length=8, default="")
    node = models.CharField('Jenkins Node', max_length=64, default="")
    result = models.CharField('Result', max_length=64, default="")
    suite = models.CharField('Suite', max_length=64, default="")

    class Meta:
        db_table = "crt_load_testcase_status_page"
        unique_together = (("loadname", "casename", "btsid"),)

    def __str__(self):
        return "{}_{}".format(self.loadname, self.casename)


class JenkinsJobs(models.Model):
    job = models.CharField('Jenkins Job', max_length=255,
                           unique=True, default="")

    order = models.PositiveSmallIntegerField('order', default=0)

    class Meta:
        db_table = "crt_jenkins_job"

    def __str__(self):
        return "{}_{}".format(self.job, self.order)


class JenkinsInfo(models.Model):
    url = models.CharField('Jenkins URL', max_length=128,
                           unique=True, default="")
    user = models.CharField('Jenkins User', max_length=16, default="")
    passwd = models.CharField('Jenkins Password', max_length=16, default="")

    jobs = models.ManyToManyField(
        JenkinsJobs, through='JenkinsJobMonitor', default="")

    class Meta:
        db_table = "crt_jenkins_info"

    def __str__(self):
        return self.url


class JenkinsJobMonitor(models.Model):
    task = models.CharField('Task Name', max_length=32, default="")
    jenkins = models.ForeignKey(
        JenkinsInfo, on_delete=models.CASCADE, default="")
    job = models.ForeignKey(JenkinsJobs, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = "crt_jenkins_monitor"
        unique_together = (("task", "jenkins", "job"),)

    def __str__(self):
        return "{}_{}_{}".format(self.task, self.jenkins, self.job)

# <load--testline status>


class LoadTestlineStatus(models.Model):
    loadname = models.CharField('Load name',  max_length=64, default="")
    testline = models.CharField('Testline', max_length=64, default="")
    btsid = models.CharField(
        'BTSID', null=True, blank=True, max_length=8, default="")
    url = models.CharField('Jenkins URL', max_length=128, default="")
    job = models.CharField('Jenkins Job', max_length=255, default="")
    build_id = models.CharField('Build ID', max_length=8, default="")
    build_time = models.CharField('Build Time', max_length=32, default="")
    build_status = models.CharField(
        'Build Status', max_length=8, null=True, blank=True, default="")
    build_url = models.CharField('Build URL', max_length=512, default="")

    class Meta:
        db_table = "crt_load_testline_status_page"
        unique_together = (("loadname", "testline", "url", "job", "build_id"),)

    def __str__(self):
        return "{}_{}".format(self.loadname, self.testline)

# <load> status


class LoadStatus(models.Model):
    start_time = models.CharField('Start Time', max_length=32, default="")
    loadname = models.CharField('Load', max_length=32, unique=True, default="")
    passed_num = models.CharField('Passed', max_length=8, default="")
    failed_num = models.CharField('Failed', max_length=8, default="")
    norun_num = models.CharField('NA', max_length=8, default="")
    total_num = models.CharField('Total', max_length=8, default="")
    first_passrate = models.CharField(
        'First PassRate', max_length=8, default="")
    passrate = models.CharField('PassRate', max_length=8, default="")
    debug = models.CharField('Debug', max_length=8, default="")

    class Meta:
        db_table = "crt_loadstatus_page"

    def __str__(self):
        return self.loadname
