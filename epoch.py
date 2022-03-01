# !/bin/env python3

import argparse
import datetime

"""
python3 epoch.py --times=
"""

# Parse argument passed
parser = argparse.ArgumentParser(description='Pull passed epoch time file.')
parser.add_argument('--times', '-t', type=str, help='Raw epoch time file that will be handled', required=True)
args = parser.parse_args()

# Load passed file to list
with open(args.times) as t:
    try:
        epoch_list = [int(stamp) for stamp in t]
    except:
        print("Non-number entered, check input and try again")
        quit()

# Begin loop of converting
try:
    # Attempt in seconds first
    for i in epoch_list:
        print(datetime.datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S'))
except:
    # Attempt milliseconds
    for i in epoch_list:
        longtime = datetime.datetime.fromtimestamp(i/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
        print(longtime[:-3])
