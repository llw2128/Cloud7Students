#!/bin/bash

# Stop all supervisor-controlled processes
pkill -f python
# Deactivate the virtual environment
deactivate

echo "All servers stopped."
