#!/bin/bash

# Run git pull
git pull

# Change directory to src
# shellcheck disable=SC2164
cd ../src

# Run python parse.py
python parse.py

# Optionally, you can include a pause to see the output before the terminal closes
# shellcheck disable=SC2162
read -p "Press any key to continue..."
