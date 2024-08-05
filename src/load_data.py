# read the data from the original data source
# Save it in the data/raw for further process

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path=config_path) # Loaded the params.yaml file
    df = get_data(config_path=config_path)
    # Now in the dataset the columns are having sapeces in between which may cause us issue, hence we will replace
    new_cols=[cols.replace(" ","_") for cols in df.columns]
    # Now let's save the data in the Raw folder and the path we will get from params.yaml
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols) # Will store data in raw folder

# Now we will need a main() to execute this operation

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)