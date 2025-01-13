# Scarf Metrics
This PR introduces initial metric calculation functionalities for assessing cell population structures and integration quality in `DataStore`. Three new methods have been added to the `DataStore` class:
- `metric_lisi`: Computes the Local Inverse Simpson Index (LISI) scores to evaluate the mixing of cell populations across neighborhoods.
- `metric_silhouette`: Calculates modified silhouette scores to assess cluster separation.
- `metric_integration`: Measures alignment quality between batches using ARI or NMI.

The file `metrics.py` was added to provide implementations for these metric functions.

## 1. `metric_lisi()`
This function calculates LISI scores for cell populations. 
**Key Parameters**: `label_colnames`, `use_latest_knn`, `from_assay`.
**Return**: Optionally returns LISI scores by label if return_lisi=True

## 2. `metric_silhouette()`: 
Computes silhouette scores, adapted for use with KNN graphs.
**Key Parameters**: `use_latest_knn`, `res_label`.
**Return**: Returns an array of silhouette scores for each cluster. NaN values indicate clusters that could not be scored.

## 3. `metric_integration()`:
Calculates integration scores between batches using ARI or NMI.
**Key Parameters**: `batch_labels`, `metric` (default: `ari`).
**Return**: Returns a float between `0` and `1`, indicating alignment quality.

Examples:
```python

# Assuming `datastore.make_graph()` was run.
# Example usage of metric_lisi with default KNN
lisi_scores = datastore.metric_lisi(
    label_colnames=["cell_type"],
    save_result = False,
    return_lisi=True
)

# Assuming `datastore.run_leiden_clustering()` was run
# Example usage of metric_silhouette for cluster evaluation
silhouette_scores = datastore.metric_silhouette(
    use_latest_knn=True,
    res_label="leiden_cluster"
)

# Example usage of metric_integration to assess batch alignment
integration_score = datastore.metric_integration(
    batch_labels=["batch1", "batch2"],
    metric="ari"
)
````
