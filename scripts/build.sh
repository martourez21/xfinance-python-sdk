##!/bin/bash
## Build script for xfinance Python SDK
#
#set -e
#
#echo "Building xfinance Python SDK..."
#
## Clean up previous builds
#rm -rf build/ dist/ *.egg-info
#
## Install build dependencies
#pip install --upgrade pip
#pip install build twine
#
## Run tests first
#echo "Running tests..."
#python -m pytest tests/ -v
#
## Build the package
#echo "Building package..."
#python -m build
#
## Check the build
#echo "Checking build..."
#twine check dist/*
#
#echo "Build completed successfully!"
#echo "Packages available in dist/ directory"