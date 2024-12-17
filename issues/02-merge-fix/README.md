Logical error in `merge.py` file. The `get_feat_suffix()` results in error with weird names.

Update:
- `get_feat_suffix()` function in `merge.py` file is only run when gene ensemble IDs and names are the same (`feat_name_ids_same` is `True`) and we update the `featCollection_map` dictionary with `update_feat_ids_for_map()` function. Else, we directly copy `featCollection` to `featCollection_map`