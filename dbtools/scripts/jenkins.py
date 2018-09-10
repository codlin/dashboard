import warnings
import re
from datetime import datetime
from jenkinsapi.jenkins import Jenkins


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


class FilteredBuildInfo(object):
    def __init__(self):
        self.status = ''
        self.timestamp = ''
        self.duration = ''
        self.params = ''
        self.slave = ''
        self.url = ''


class JenkinsMonitor(object):
    def __init__(self, url, user, passwd, job_name):
        self.jenkins = Jenkins(url, user, passwd)
        self.job = self.jenkins.get_job(job_name)

    def get_last_build(self):
        return self.job.get_last_build()

    def get_first_buildnumber(self):
        return self.job.get_first_buildnumber()

    def get_last_buildnumber(self):
        return self.job.get_last_buildnumber()

    # return build number (int)
    def get_builds_number(self):
        return self.job.get_build_ids()

    def get_build(self, build_num):
        return self.job.get_build(int(build_num))

    def get_build_json(self, build_num):
        return self.get_build(build_num)._data

    def get_lastbuild_by(self, load_name):
        first_build_number = self.get_first_buildnumber()
        last_build_number = self.get_last_buildnumber()
        for number in range(first_build_number, last_build_number)[::-1]:
            build = self.get_build(number)
            if load_name in build.get_params().values():
                return build

        raise ValueError()

    def get_build_console_url(self, build_num):
        build = self.get_build(build_num)
        return '{}/console'.format(build.baseurl)

    def get_build_timestamp(self, build_num):
        build = self.get_build(build_num)
        timestamp = build._data['timestamp']
        return convertToDateTime(timestamp)

    def get_build_duration(self, build_num):
        build = self.get_build(build_num)
        return build._data["duration"]

    def getFilteredBuildInfo(self, build_num):
        build = self.get_build(build_num)

        info = FilteredBuildInfo()
        info.status = build.get_status()
        info.timestamp = self.get_build_timestamp(build_num)
        info.duration = self.get_build_duration(build_num)
        info.params = build.get_params()
        info.slave = build.get_slave() or 'master'
        info.url = self.get_build_console_url(build_num)

        return info


# test
if __name__ == "__main__":
    monitor = JenkinsMonitor('http://10.52.200.190', 'scpadm',
                             'scpadm', 'check_site_state_FDD_AICT3')

    builds = monitor.get_builds_number()
    s = map(str, builds)
    print(', '.join(s))

    info = monitor.getFilteredBuildInfo(s[0])
    print(info.timestamp, info.duration, info.status,
          info.slave, info.url, info.params)
