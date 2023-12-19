#!/bin/bash
sudo pkill -f python
cd /home/ec2-user/Cloud7Students/
sudo chmod -R 777 ./
nohup python3 /home/ec2-user/Cloud7Students/main.py > output.log 2>&1 &