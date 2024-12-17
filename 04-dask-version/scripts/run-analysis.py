import sys
sys.path.append("..")

import time
import os
import numpy as np
from scarf import scarf
from utils.monitor_ram import monitor_ram
import pickle as pkl

def get_dataset_names() -> np.ndarray:
    files = np.sort(os.listdir("../data"))
    return files

def main(dask_version:str)->None:
    # print the dask version
    print("+"*50)
    print(f"Dask version: {dask_version}")
    dataset_names = get_dataset_names()
    
    results = {}
    results['das_version'] = dask_version
    
    for dataset_name in dataset_names:
        print("#"*50)
        print(f"Processing {dataset_name}")
        ds = scarf.DataStore(
            zarr_loc = f"../data/{dataset_name}"
        )
        ds_rna = ds.RNA
        
        start_time = time.time()
        
        ram_ds = monitor_ram(
            ds_rna.set_feature_stats,
            cell_key='I',
            use_existing=False
        )
        
        end_time = time.time()

        results[dataset_name] = {
            "time": end_time - start_time,
            "ram": ram_ds
        }
        print(f"\tTime taken: {end_time - start_time} seconds")
        print("#"*50)
    print("+"*50)

    os.makedirs(f"../results/{dask_version}", exist_ok=True)
    with open(f"../results/{dask_version}/results.pkl", "wb") as f:
        pkl.dump(results, f)

if __name__ == "__main__":
    dask_version = os.getenv("DASK_VERSION")
    print(f"Running analysis for Dask version: {dask_version}")
    if dask_version is None:
        raise ValueError("DASK_VERSION environment variable not set")
    main(dask_version)