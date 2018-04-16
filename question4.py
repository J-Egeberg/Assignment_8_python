from common_functions import get_csv_reader

def run(f):
    reader = get_csv_reader(f)

    successful_count = 0
    for row in reader:
        state = row[9] == "successful"
        enough_pledged = float(row[13]) > 5000
        if state and enough_pledged:
            successful_count += 1

    print(successful_count)
