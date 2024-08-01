## read params
## process
## return dataframe

import os
import yaml
import pandas as pd
import argparse

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_arguemnt("--config",default="params.yaml")