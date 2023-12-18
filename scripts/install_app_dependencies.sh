#!/bin/bash
sudo pip3 install virtualenv
cd /home/ec2-user/Cloud7Students
virtualenv environment
source environment/bin/activate
sudo pip3 install -r requirements.txt