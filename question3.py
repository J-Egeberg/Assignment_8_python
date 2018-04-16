from common_functions import get_csv_reader, each_funded_project


def run(f):
    reader = get_csv_reader(f)
    pledged_amounts = []
    each_funded_project(reader, lambda row: pledged_amounts.append(row[12]))
    pledged_amounts.sort()
    median = pledged_amounts[len(pledged_amounts) // 2]
    print(median)
