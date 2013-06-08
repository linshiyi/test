#!/bin/bash
# cut_log.sh
# author: hz_linyu@2013-05-13 15:37   1th
# This script run at 00:00
# purpose: cut logs everyday.

# The logs path
logs_path='/home/nginx/logs/'

mkdir -p ${logs_path}$(date -d "yesterday" +%Y)/$(date -d "yesterday" +%m)/
mv ${logs_path}access.log ${logs_path}$(date -d "yesterday" +%Y)/$(date -d "yesterday" +%m)/access_$9(date -d "yesterday" +%Y%m%d).log

kill -USR1 `cat /usr/local/xxx.pid`



