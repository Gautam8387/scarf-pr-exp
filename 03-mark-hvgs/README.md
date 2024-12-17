# PR for Updating `mark_hvgs()` in assay.py


1. Separated summary statistics calculation from mark_hvgs()
2. Performed some type checking


The notebook `summary-stat-checks.ipynb` have examples of the changes made to the function. We also run multiple iterations of the function with different parameters to check if the function is working as expected. Tested both `set_summary_stats()` and `mark_hvgs()` functions.


To calculate summary statistics:
```python
import scarf

ds = scarf.DataStore('path/to/dataset.zarr')

ds.RNA.set_summary_stats(
    n_bins=bin, # integer
    lowess_frac=frac # float
)
```