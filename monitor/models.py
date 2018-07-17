from djongo import models

class LoadJobStatus(models.Model):
    job_name = models.CharField(max_length=256)
    build_on = models.CharField(max_length=16)
    build_num = models.CharField(max_length=8)
    build_result = models.CharField(max_length=8)
    timestamp = models.DateTimeField('build time')

    def __str__(self):
        return self.job_name

class LoadPipeline(models.Model):
    load_name = models.CharField(max_length=30)
    root_buildnum = models.IntegerField()
    
    jobs = models.ArrayModelField(model_container=LoadJobStatus, )

    def __str__(self):
        return self.load_name
    