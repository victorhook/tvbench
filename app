#!/bin/bash

source env/bin/activate
export FLASK_APP=tvbench/app.py
export FLASK_ENV=development
flask run