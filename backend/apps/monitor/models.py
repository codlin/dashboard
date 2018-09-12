from django.db import models
import djongo.models

# <product id>
# CRT product data, e.g.:
# fzmfdd: 'FZM FDD'
# cfzcfdd: 'CFZC TDD'


class Product(models.Model):
    name = models.CharField('Product Name', max_length=16, default="")
    text = models.CharField('Product Text', max_length=16, default="")

    class Meta:
        db_table = "crt_product"

    def __str__(self):
        return self.name

# <system menu>


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

#------------------testline table-----------------------#
# <testline>


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


#------------------case-related table-----------------------#
# <case path>


class TesecasePath(models.Model):
    path = models.CharField('Case path', max_length=255,
                            unique=True, default="")

    class Meta:
        db_table = "crt_testcasepath"

    def __str__(self):
        return self.path

# <testcase>


class Testcase(models.Model):
    casename = models.CharField(
        'Case name', max_length=255, unique=True, default="")
    path = models.ForeignKey(
        TesecasePath, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = "crt_testcase"

    def __str__(self):
        return self.casename

# <release -- testcase>


class TestcaseRelease(models.Model):
    load_release = models.CharField(
        'Release', max_length=16, default="")
    case = models.ForeignKey(Testcase, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = "crt_testcase_release"

    def __str__(self):
        return "{}_{}".format(self.load_release, self.case)

# <load--testcase--testline> scheduler


class LoadTestcaseSchedule(models.Model):
    loadname = models.CharField(
        'Load Name', max_length=64, default="")
    case = models.ForeignKey(Testcase, on_delete=models.DO_NOTHING, default="")
    btsid = models.CharField('BTSID', max_length=8, default="")

    class Meta:
        db_table = "crt_load_testcase_schedule"

    def __str__(self):
        return "{}_{}_{}".format(self.loadname, self.btsid, self.case)

#------------------run history table-----------------------#
# <load--testcase status>


class LoadTestcaseStatus(models.Model):
    loadname = models.CharField('Load name', max_length=64, default="")
    casename = models.CharField('Case name', max_length=255, default="")
    btsid = models.CharField('BTSID', max_length=8, default="")
    node = models.CharField('Jenkins Node', max_length=64, default="")
    result = models.CharField('Result', max_length=64, default="")
    suite = models.CharField('Suite', max_length=64, default="")

    class Meta:
        db_table = "crt_load_testcase_status_page"
        unique_together = ("loadname", "casename", "btsid")

    def __str__(self):
        return "{}_{}".format(self.loadname, self.casename)


class JenkinsJobs(models.Model):
    job = models.CharField('Jenkins Job', max_length=255,
                           unique=True, default="")

    class Meta:
        db_table = "crt_jenkins_job"

    def __str__(self):
        return self.job


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
    jobs = models.ForeignKey(JenkinsJobs, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = "crt_jenkins_monitor"
        unique_together = ("task", "jenkins", "jobs")

    def __str__(self):
        return "{}_{}_{}".format(self.task, self.jenkins, self.jobs)

# <load--testline status>


class LoadTestlineStatus(models.Model):
    loadname = models.CharField('Load name', max_length=64, default="")
    testline = models.CharField('Testline', max_length=64, default="")
    btsid = models.CharField('BTSID', max_length=8, default="")

    url = models.ForeignKey(
        JenkinsInfo, related_name='jenkins_url', on_delete=models.DO_NOTHING, default="")
    job = models.ForeignKey(
        JenkinsJobs, related_name='job_name', on_delete=models.DO_NOTHING, default="")
    build_id = models.CharField('Build ID', max_length=8, default="")
    build_time = models.CharField('Build Time', max_length=32, default="")
    build_status = models.CharField(
        'Build Status', max_length=8, null=True, blank=True, default="")
    build_url = models.CharField('Build URL', max_length=512, default="")

    class Meta:
        db_table = "crt_load_testline_status_page"
        unique_together = ("loadname", "btsid")

    def __str__(self):
        return "{}_{}".format(self.loadname, self.btsid)

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
