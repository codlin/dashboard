import warnings

from jenkinsapi.jenkins import Jenkins

class FilteredBuildInfo(object):
    def __init__(self):
        self.status = ''
        self.timestamp = ''
        self.duration = ''
        self.params = ''
        self.slave = ''

class LoadPipeline(object):
    def __init__(self):
        self.load_name = ''
        self.root_buildnum = ''
        self.jobs = list()
    
class JenkinsMonitor(object):
    def __init__(self, url, user, passwd):
        self.jenkins = Jenkins(url, user, passwd)
        pass
    
    def get_last_build(job_name):
        job = self.jenkins.get_job(job_name)
        return job.get_last_build()
    
    def get_last_buildnumber(job_name):
        job = self.jenkins.get_job(job_name)
        return job.get_last_buildnumber()

    def get_build(job_name, build_num):
        job = self.jenkins.get_job(job_name)
        return job.get_build(int(build_num))
    
    def get_build_json(job_name, build_num):
        warnings.warn(
            "This untested function may soon be removed from JenkinsMonitor "
            "(get_build_json).")

        return self.get_build(job_name, build_num)._data
    
    def getFilteredBuildInfo(job_name, build_num, filter=None):
        build = self.get_build_detail(job_name, build_num)
        info = FilteredBuildInfo()

        info.status = build.get_status()
        info.timestamp = build.get_timestamp()
        info.duration = build.get_duration()
        info.params = build.get_params()
        info.slave = build.get_slave() or 'master'

        return info
    
    def getLoadPipline(load_name, job_list):
        root_job = job_list[0]
        root_buildnum = self.get_last_buildnumber(root_job)

        pipeline = LoadPipeline()
        pipeline.load_name = load_name
        pipeline.root_buildnum = root_buildnum

        for job in job_list:
            buildnum = self.get_last_buildnumber(job)
            buildinfo = self.getFilteredBuildInfo(job, buildnum)
            pipeline.jobs.append(buildinfo)
        
        return pipeline
