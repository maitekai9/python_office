#!/bin/bash
cur_dir=$(cd $(dirname $0); pwd)
echo $cur_dir
file_name=$(ls -lt $cur_dir | grep 'xlsx' | head -n 1 |awk '{print $9}')
echo $file_name
python /f/python/python_office/office/get_ason.py $file_name
