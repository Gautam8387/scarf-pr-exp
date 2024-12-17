# CrDriReader Update

Update 1:
Rolling back to `pandas` from `polars` for the time being. The `polars` library is not yet mature enough to handle compressed files resulting in large memory footprints for `_get_valid_barcodes()` function. 

Update 2:
Rolling back to `pandas` from `polars` for the time being. Same issue as above in `consume()` function.


The notebook `consume.ipynb` has shows the memory footprint of the `_get_valid_barcodes()` and `consume()` functions for the updated `CrDirReader` class on a `783K` cell dataset. The memory footprint is significantly lower and bounded for `pandas` compared to `polars`.