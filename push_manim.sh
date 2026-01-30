#!/bin/bash
# Navigate to the project folder
cd "$(dirname "$0")"

# Stage all changes
git add .

# Commit with a default message including timestamp
git commit -m "Update $(date '+%Y-%m-%d %H:%M:%S')"

# Push to main branch
git push origin main