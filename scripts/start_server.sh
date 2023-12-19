#!/bin/bash
cd /home/ec2-user/Cloud7Students/
#source environment/bin/activate
#supervisord -c supervisord.conf
nohup python3 /home/ec2-user/Cloud7Students/main.py > output.log 2>&1 &