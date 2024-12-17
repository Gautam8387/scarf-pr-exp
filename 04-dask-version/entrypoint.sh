#!/bin/bash

# Check if DASK_VERSION is provided
if [ -z "$DASK_VERSION" ]; then
    echo "Error: DASK_VERSION environment variable is required"
    exit 1
fi

# Create results directory for this dask version
mkdir -p /results/$DASK_VERSION

# Install specific dask version
pip uninstall -y dask==$DASK_VERSION
pip install dask==$DASK_VERSION

# Run the analysis
cd /scripts
python run-analysis.py

# Uninstall dask
pip uninstall -y dask
pip uninstall -y dask==$DASK_VERSION

exit 0