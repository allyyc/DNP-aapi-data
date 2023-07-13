import pandas as pd
import csv
import itertools
from argparse import ArgumentParser
import os

# COMMAND: python txt_to_csv.py --train_dataset [dataset_name]
argp = ArgumentParser()
argp.add_argument("--train_dataset", required=True)
args = argp.parse_args()

# DATASET
if not os.path.exists(args.train_dataset):
    raise RuntimeError(f"Failed to load TRAIN_DATASET <{args.train_dataset}>: no such file exists.")

with open(args.train_dataset, 'r') as infile:
    stripped = (line.strip() for line in infile)
    lines = (line.split("|") for line in stripped if line)

    with open(args.train_dataset[0:-4]+'.csv', 'w') as outfile:

        count = 0  # Initialize a counter
        writer = csv.writer(outfile)

        for line in lines:
            writer.writerow(line)
            count += 1
            print(count)


