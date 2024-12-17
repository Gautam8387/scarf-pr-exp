This repository contains the code and results for the benchmark of all releases of `dask` 2024 for the use of `scarf` library.

We found that the performance of `dask` decreased after the July 2024 release. The release of `dask` in July 2024 was the last release that showed a good performance. After that, the performance of `dask` decreased significantly resulting in large memory consumptions.

The `2024.7.1` release of `dask` took `721.50390625 MB` of memory for computing summary statistics of a dataset of size `1.3M` cells. All the releases after that took more than `34 GB` of memory for the same computation.


Detailed results can be found in the `results` directory. The workflow is explained in `workflow.md` file. The `dask_versions.txt` file contains the list of all the 2024 releases of `dask` that were benchmarked.