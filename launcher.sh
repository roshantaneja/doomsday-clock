#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

#!/bin/bash

# Get the directory of the script itself
script_dir=$(dirname "$0")

# Navigate to that directory
cd "$script_dir"

# Now you are in the same directory as the script file
echo "Current directory:"
pwd


git stash
git pull
python3 doomsday.py
