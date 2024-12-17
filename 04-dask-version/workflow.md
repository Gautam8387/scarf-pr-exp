The working directory contains following file files and directories:
```
.
├── dask_versions.txt
├── data
├── notebooks
├── raw
├── requirements.txt
├── results
├── scarf
├── scripts
└── utils

7 directories, 2 files
```
We create a docker image which contains the following:
```
1. Python 3.11
2. ./scripts copied to /scripts
3. ./utils copied to /utils
4. ./scarf copied to /scarf
5. ./requirements.txt copied to /requirements.txt
```
We edited the `assay.py` in scarf library to include an argument `use_existing` in `set_feature_stats()` function. We pass this argument as `False`. This is to ensure that the summary statistics are computed again and not loaded from the cache.

Then we install all the `pip` dependencies in the requirements.txt file.

We pass on a `dask` version to the docker image and it installs the that specific version of `dask` and run the following command:
```bash
python scripts/run-analysis.py
```
The `run-analysis.py` script is located in the `scripts` directory. It will read the data from the `data` directory. The results are stored in the `results/<dask-version>` directory. The `data` and `results` directory is outside the docker container and are mounted to the docker container at the time of running the docker image.

After this, we uninstall the `dask` version and get ready for the next `dask` version and repeat the process.