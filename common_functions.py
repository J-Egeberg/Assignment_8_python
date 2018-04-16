import csv


def get_csv_reader(f):
    f.seek(0)
    reader = csv.reader(f, delimiter=',')
    next(reader)
    return reader


def each_funded_project(reader, callback):
    for row in reader:
        state = row[9]
        if state == "successful":
            callback(row)
