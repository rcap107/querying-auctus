#%%
import polars as pl
from pathlib import Path

#%% 
import os
os.chdir(Path("~/work/prepare-data-lakes/").expanduser())
# %%
data_path = Path("data/auctus")
csv_path = Path(data_path, "csv")
pq_path = Path(data_path, "parquet")

# %%
count = 0 

for tab_path in csv_path.glob("**/*.csv"):
    print(tab_path)
    print(count)
    df = pl.read_csv(tab_path, infer_schema_length=0)
    new_name = tab_path.stem + ".parquet"
    df.write_parquet(Path(pq_path, new_name))
    count +=1
# %%
