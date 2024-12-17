while IFS= read -r version || [ -n "$version" ]; do
    rm -rf output.log
    version=$(echo "$version" | tr -d '\r')
    echo "Starting analysis for dask version: $version" | tee -a output.log
    if sudo docker run \
        -e DASK_VERSION="$version" \
        -v "$(pwd)/results:/results" \
        -v "/media/chs.gpu/nygen/dask-version/data:/data" \
        dask-analysis >> output.log 2>&1; then
        echo "Successfully completed analysis for dask version: $version" | tee -a output.log
    else
        echo "Error occurred with dask version: $version" | tee -a output.log
        echo "Continuing with next version..." | tee -a output.log
    fi
done < dask_versions.txt
