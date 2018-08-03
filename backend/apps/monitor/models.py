from django.db import models
import djongo.models

class Product(models.Model):
    name = models.CharField('Name', max_length=16)
    text = models.CharField('Text', max_length=16)
    class Meta:
        db_table = "crtdashboard_product"

    def __str__(self):
        return self.name

class SysMenu(models.Model):
    index = models.PositiveSmallIntegerField('Index')
    level = models.PositiveSmallIntegerField('Level')
    group = models.CharField('Group', max_length=8)
    name = models.CharField('Name', max_length=16)
    text = models.CharField('Text', max_length=16)
    class Meta:
        db_table = "crtdashboard_sysmenu"

    def __str__(self):
        return self.name
    
class LoadStatus(models.Model):
    start_time = models.DateTimeField('Start Time')
    load_name = models.CharField('Load', max_length=30)
    passed_num = models.PositiveIntegerField('Passed')
    failed_num = models.PositiveIntegerField('Failed')
    norun_num = models.PositiveIntegerField('NA')
    total_num = models.PositiveIntegerField('Total')
    first_passrate = models.FloatField('First PassRate')
    passrate = models.FloatField('PassRate')
    class Meta:
        db_table = "crtdashboard_loadstatus"

    def __str__(self):
        return self.load_name

# class LoadJobStatus(djongo.models.Model):
#     job_name = djongo.models.CharField(max_length=256)
#     build_on = djongo.models.CharField(max_length=16, default='master')
#     build_num = djongo.models.PositiveIntegerField()
#     build_result = djongo.models.CharField(max_length=8)
#     timestamp = djongo.models.DateTimeField('build time')

#     class Meta:
#         abstract = True

# class LoadPipeline(djongo.models.Model):
#     load_name = djongo.models.CharField(max_length=30)
#     root_buildnum = djongo.models.PositiveIntegerField()
#     start_time = djongo.models.DateTimeField('start time')

#     jobs = djongo.models.ArrayModelField(model_container=LoadJobStatus)

#     def __str__(self):
#         return self.load_name
