#!/bin/bash
cd endorsement-api
pwd
source venv/bin/activate
sls wsgi serve --host=0.0.0.0