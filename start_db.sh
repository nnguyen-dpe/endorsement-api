#!/bin/bash
python db.py db init
python db.py db migrate
python db.py db upgrade