import warnings
import re
from abc import abstractmethod
from datetime import datetime
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.job import Job
from jenkinsapi.build import Build


def convertToDateTime(timestamp):
    if isinstance(timestamp, (int, float, str)):
        try:
            timestamp = int(timestamp)
        except ValueError:
            raise
        if len(str(timestamp)) == 13:
            timestamp = int(timestamp / 1000)
        if len(str(timestamp)) != 10:
            raise ValueError
    else:
        raise ValueError()
    d = datetime.fromtimestamp(timestamp)
    result = d.strftime("%Y-%m-%d %H:%M:%S")
    return result


'''
job methods:
get_first_buildnumber()
get_last_buildnumber()
get_build_ids()
build = get_build(int(build_num))
get_build_json(build)

build methods:
build.get_params()

get_build_console_url(build)
get_build_timestamp(build)
get_build_duration(build)
'''


class JenkinsJobBuild(object):
    def __init__(self, build):
        self._build = build

    @property
    def info(self):
        return self._build

    @property
    def json_data(self):
        return self._build._data

    @property
    def console_url(self):
        return '{}/console'.format(self._build.baseurl)

    @property
    def timestamp(self):
        return convertToDateTime(self.json_data['timestamp'])

    @abstractmethod
    def getFilteredBuildInfo(self, filter_params={}):
        pass


class JenkinsMonitor(object):
    def __init__(self, url, user, passwd):
        self.jenkins = Jenkins(url, user, passwd)
        self.jobs = dict()

    def add_job(self, job_name):
        if job_name in self.jobs.keys():
            return

        self.jobs[job_name] = self.jenkins.get_job(job_name)
        return self.jobs[job_name]

    def remove_job(self, job_name):
        if job_name in self.jobs.keys():
            return self.jobs.pop(job_name)

        return None

    # return dict(job_name, job)
    def get_monitor_jobs(self):
        return self.jobs


# test
if __name__ == "__main__":
    monitor = JenkinsMonitor('http://10.52.200.190', 'scpadm', 'scpadm')

    job = monitor.add_job('check_site_state_FDD_AICT3')
    # builds = job.get_build_ids()
    # s = map(str, builds)
    # print(', '.join(s))

    build = JenkinsJobBuild(job.get_build(job.get_last_buildnumber()))
    print("info: ", build.info)
    print("params: ", build.info.get_params())
    print("json data: ", build.json_data)
    print("console url: ", build.console_url)
    print("timestamp: ", build.timestamp)
