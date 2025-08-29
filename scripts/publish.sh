##!/bin/bash
## Publish script for xfinance Python SDK
#
#set -e
#
#echo "Publishing xfinance Python SDK..."
#
## Check if we're on main branch
#CURRENT_BRANCH=$(git branch --show-current)
#if [ "$CURRENT_BRANCH" != "main" ]; then
#    echo "Error: Must be on main branch to publish"
#    exit 1
#fi
#
## Check if working directory is clean
#if [ -n "$(git status --porcelain)" ]; then
#    echo "Error: Working directory is not clean"
#    exit 1
#fi
#
## Build the package
#echo "Building package..."
#./scripts/build.sh
#
## Publish to PyPI
#echo "Publishing to PyPI..."
#python -m twine upload dist/*
#
## Tag the release
#VERSION=$(python -c "from xfinance_sdk import __version__; print(__version__)")
#echo "Creating tag v$VERSION..."
#git tag -a "v$VERSION" -m "Release v$VERSION"
#git push origin "v$VERSION"
#
#echo "Publication completed successfully!"