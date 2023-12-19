#!/bin/bash
cd /home/ec2-user/Cloud7Students/
sudo chmod 777 .
nohup python3 /home/ec2-user/Cloud7Students/main.py > output.log 2>&1 &