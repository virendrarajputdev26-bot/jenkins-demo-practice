#!/bin/bash
set -e
echo "================================="
echo "Starting Build"
echo "================================="
echo "Python version:"
python3 --version
echo "Running application..."
python3 app/app.py
echo "Build completed successfully."
Make it executable:
chmod +x build.sh
