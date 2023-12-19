#!/bin/bash

# Stop all supervisor-controlled processes
sudo unlink /tmp/supervisor.sock
# Deactivate the virtual environment
deactivate

echo "All servers stopped."
