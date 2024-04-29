#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 to run this script."
    exit 1
fi

# Run the Python script
python3 mcstatus-ui.py
