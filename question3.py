from common_functions import get_csv_reader, each_funded_project
import numpy as np


def run(f):
    reader = get_csv_reader(f)
    pledged_amounts = []

    def add_pledged_amount(row):
        pledged_amount = row[13]
        if pledged_amount.strip() != '':
            pledged_amounts.append(float(pledged_amount))

    each_funded_project(reader, add_pledged_amount)
    pledged_amounts.sort()
    median = np.median(pledged_amounts)
    print(median)
