Fixed a critical error in `DatasetMerge` which caused the mixing up of cells in the merged dataset. The error was due to the incorrect handling of the randomized indexs when dumping the dataset. The issue is now fixed and the merged dataset is now correctly generated. 

The working example in the `merge.ipynb` notebook has been updated to reflect the changes.