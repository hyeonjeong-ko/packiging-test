#!/bin/sh -l

echo "Hello entry"

# Grant execute permission to all files in the directory
chmod +x *

ls

cd ./app

python test.py
