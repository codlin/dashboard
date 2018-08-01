# build stage django
# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7

ENV REFRESHED_AT 2018-08-01
ENV http_proxy http://135.245.48.34:8000
ENV https_proxy http://135.245.48.34:8000

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=dashboard Version=0.0.1
EXPOSE 8000

WORKDIR /app
ADD requirements.txt /app

# Using pip:
RUN python3 -m pip install -r requirements.txt

ENV http_proxy ""
ENV https_proxy ""

CMD ["python3", "manage.py runserver 0:8000"]
