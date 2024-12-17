I have the following file files and directories:
```
(scarf-dev) chs.gpu@welcome-trust-1:/media/chs.gpu/nygen/dask-version$ tree -L 1 
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
My task is as follows:
I want to create a docker image which contains the following:
```
1. Python 3.11
2. ./data should be copied to /data
3. ./scripts should be copied to /scripts
4. ./utils should be copied to /utils
5. ./scarf should be copied to /scarf
6. ./requirements.txt should be copied to /requirements.txt
```
It should install all the `pip` dependencies in the requirements.txt file.

Then I will pass on a `dask` version to the docker image and it should that specific version of `dask` and run the following command:
```bash
python scripts/run-analysis.py
```
The `run-analysis.py` script is located in the `scripts` directory. It will read the data from the `data` directory. It should write the results to the `results/<dask-version>` directory. The `results` directory is outside the docker container and should be mounted to the docker container.

After this, it should uninstall the `dask` version and get ready for the next `dask` version and repeat the process.