# !/bin/env python3

import argparse

"""
python3 epoch.py --times=
"""

# Parse argument passed
parser = argparse.ArgumentParser(description='Pull passed epoch time file.')
parser.add_argument('--times', '-t', type=str, help='Raw epoch time file that will be handled', required=True)
args = parser.parse_args()

# Load passed file to list
epoch_list = open(args.times,)
