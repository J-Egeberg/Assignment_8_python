from common_functions import get_csv_reader

def run(f):
    reader = get_csv_reader(f)

    for row in reader:
        successful_count = 0
        state = row[9]
        enough_pledged = row[13] > 5000
        if state and enough_pledged:
            successful_count += 1

    print(successful_count)
