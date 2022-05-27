#!/bin/bash
rm -rf dist
echo "start building...."
mkdir dist

echo "copy deps dir & project dir to dist .."
cp -r lib/python3.6/site-packages/* dist/
cp -r djangodemo dist/djangodemo

echo "copy files to dist .."
cp manage.py dist/
cp requirements.txt dist/
cp scf_bootstrap dist/
cp serverless.yml dist/

echo 'done!'