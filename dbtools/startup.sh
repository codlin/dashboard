#!/usr/bin/bash

echo "shedule's begining..."

log_level="INFO"
if [ -n "$1" ]; then
   log_level = $1
fi

echo "log level: ${log_level}"
python scheduler.py ${log_level}