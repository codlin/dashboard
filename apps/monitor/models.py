from djongo import models

class LoadJobStatus(models.Model):
    job_name = models.CharField(max_length=256)
    build_on = models.CharField(max_length=16, default='master')
    build_num = models.PositiveIntegerField()
    build_result = models.CharField(max_length=8)
    timestamp = models.DateTimeField('build time')

    class Meta:
            abstract = True

class LoadPipeline(models.Model):
    load_name = models.CharField(max_length=30)
    root_buildnum = models.PositiveIntegerField()
    start_time = models.DateTimeField('start time')
    
    jobs = models.ArrayModelField(model_container=LoadJobStatus)

    def __str__(self):
        return self.load_name
    