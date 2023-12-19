#!/bin/bash

# Stop all supervisor-controlled processes
supervisorctl -c /home/ec2-user/app/supervisord.conf stop all

# Deactivate the virtual environment
deactivate

echo "All servers stopped."
