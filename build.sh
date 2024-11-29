#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip

pip install -r requirements.txt

# DB Migration

# Init migration folder
# flask db init # to be executed only once

flask db migrate # Generate migration SQL
flask db upgrade # Apply changes
