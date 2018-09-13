import warnings
import re
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


class JenkinsJobBuild(object):
    '''
    build methods:
    build.get_params()
    get_build_json(build)
    get_build_console_url(build)
    get_build_timestamp(build)
    get_build_duration(build)
    '''

    def __init__(self, build):
        self._build = build

    @property
    def json_data(self):
        return self._build._data

    @property
    def console_url(self):
        return '{}/console'.format(self._build.baseurl)

    @property
    def timestamp(self):
        return convertToDateTime(self.json_data['timestamp'])


class JenkinsJob(object):
    '''
    job methods:
    get_first_buildnumber()
    get_last_buildnumber()
    get_build_ids()
    build = get_build(int(build_num))
    '''

    def __init__(self, url, user, passwd, job_name):
        self.jenkins = Jenkins(url, user, passwd)
        self.job = self.jenkins.get_job(job_name)

    def get_build(self, build_num):
        return JenkinsJobBuild(self.job.get_build(build_num))

    def get_last_buildnumber(self):
        return self.job.get_last_buildnumber()

    def get_last_build(self):
        return JenkinsJobBuild(self.job.get_last_build())

    def get_first_buildnumber(self):
        return self.job.get_first_buildnumber()

    def get_first_build(self):
        return JenkinsJobBuild(self.job.get_first_build())

    def get_build_ids(self):
        self.job.get_build_ids()

    @property
    def job(self):
        return self.job


if __name__ == "__main__":
    pass
