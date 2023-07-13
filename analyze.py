import pandas as pd
from argparse import ArgumentParser
import os

# COMMAND: python analyze.py --train_dataset [dataset.csv]

argp = ArgumentParser()
argp.add_argument("--train_dataset", required=True)
args = argp.parse_args()

df = pd.read_csv(args.train_dataset)
print("Number of entries: ", len(df))
print("Header:", df.head())
print()

def getAcceptanceOfDemo(demo_name, demo_num):
    demo_df = df[df['applicant_race_1'] == demo_num]
    demo_df_count = len(demo_df)
    approved_count = len(demo_df[(demo_df['action_taken'] == 1)])
    if demo_df_count != 0:
        approved_percent = approved_count/demo_df_count
    else:
        approved_percent = 0
    print("Number of " + demo_name + " applicants: ", demo_df_count)
    print("Number of " + demo_name + " applicants whose loan was approved and accepted: ", approved_count)
    print("Percentage: ", approved_percent)

demographics = [["American Indian or Alaska Native", 1], ["Asian", 2], ["Asian Indian", 21], ["Chinese", 22], ["Filipino", 23],
    ["Japanese", 24], ["Korean", 25], ["Vietnamese", 26], ["Other Asian", 27], ["Black or African American", 3],
    ["Native Hawaiian or Other Pacific Islander", 4], ["Native Hawaiian", 41], ["Guamanian or Chamorro", 42], ["Samoan", 43],
    ["Other Pacific Islander", 44], ["White", 5]] 

for demographic in demographics:
    getAcceptanceOfDemo(demographic[0], demographic[1])