import warnings
import re

from datetime import datetime

from jenkinsapi.jenkins import Jenkins


def convertToDateTime(timestamp):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')


def getLoadName(jenkins_params_dict):
    for _, v in jenkins_params_dict:
        if re.match(r'[F|T]L[F|C]', v):
            return v

    return ''


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
        self.start_time = ''
        self.jobs = list()


class JenkinsMonitor(object):
    def __init__(self, url, user, passwd):
        self.jenkins = Jenkins(url, user, passwd)
        pass

    def get_last_build(self, job_name):
        job = self.jenkins.get_job(job_name)
        return job.get_last_build()

    def get_last_buildnumber(self, job_name):
        job = self.jenkins.get_job(job_name)
        return job.get_last_buildnumber()

    def get_build(self, job_name, build_num):
        job = self.jenkins.get_job(job_name)
        return job.get_build(int(build_num))

    def get_build_json(self, job_name, build_num):
        warnings.warn(
            "This untested function may soon be removed from JenkinsMonitor "
            "(get_build_json).")

        return self.get_build(job_name, build_num)._data

    def get_lastbuild_by(self, job_name, load_name):
        job = self.jenkins.get_job(job_name)
        first_build_number = job.get_first_buildnumber()
        last_build_number = self.get_last_buildnumber()
        for number in range(first_build_number, last_build_number)[::-1]:
            build = self.get_build(number)
            if load_name in build.get_params().values():
                return build

        raise ValueError()

    def getFilteredBuildInfo(self, job_name, build_num, filter=None):
        build = self.get_build(job_name, build_num)
        info = FilteredBuildInfo()

        info.status = build.get_status()
        info.timestamp = build.get_timestamp()
        info.duration = build.get_duration()
        info.params = build.get_params()
        info.slave = build.get_slave() or 'master'

        return info

    def getLoadPipline(self, job_list, build_num=None):
        root_job = job_list[0]
        if build_num:
            root_buildnum = int(build_num)
        else:
            root_buildnum = self.get_last_buildnumber(root_job)

        root_build = self.getFilteredBuildInfo(root_job, root_buildnum)

        pipeline = LoadPipeline()
        pipeline.load_name = getLoadName(root_build.params)
        pipeline.root_buildnum = root_buildnum
        pipeline.start_time = root_build.timestamp

        pipeline.jobs.append(root_build)
        for job in job_list[1:]:
            buildnum = self.get_last_buildnumber(job)
            buildinfo = self.getFilteredBuildInfo(job, buildnum)
            pipeline.jobs.append(buildinfo)

        return pipeline
