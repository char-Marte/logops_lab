#!/bin/bash

echo "===== SYSTEM LOG REPORT ====="
echo "User: $(whoami)"
echo "Current directory: $(pwd)"
echo "Date: $(date)"
echo "Errors found: $(grep "ERROR" app.log | wc -l)"
echo "Warnings found: $(grep "WARNING" app.log | wc -l)" 
echo "============================"
