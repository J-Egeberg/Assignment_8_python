import operator

from common_functions import get_csv_reader, each_funded_project


def run(f):
    reader = get_csv_reader(f)

    main_cat_success_counts = {}

    def add_count_to_main_category(row):
        main_category = row[3]
        main_cat_success_counts.setdefault(main_category, 0)
        main_cat_success_counts[main_category] += 1

    each_funded_project(reader, add_count_to_main_category)

    restart_pointer(f)

    all_main_cat_counts = get_all_main_cat_counts(reader)

    main_cat_success_rates = get_main_cat_sucess_rates(all_main_cat_counts, main_cat_success_counts)

    best_main_category = max(main_cat_success_rates.items(), key=operator.itemgetter(1))

    print(best_main_category[0] + " has the best succes rate with a " + str(best_main_category[1]) + " success rate.")
    return best_main_category[0]


def get_main_cat_sucess_rates(all_main_cat_counts, main_cat_success_counts):
    main_cat_success_rates = {}
    for item in all_main_cat_counts.items():
        all_cat_count = item[1]
        cat = item[0]
        successful_can_count = main_cat_success_counts[cat]
        main_cat_success_rates[cat] = (successful_can_count * 100) / all_cat_count
    return main_cat_success_rates


def get_all_main_cat_counts(reader):
    all_main_cat_counts = {}
    for row in reader:
        main_category = row[3]
        all_main_cat_counts.setdefault(main_category, 0)
        all_main_cat_counts[main_category] += 1
    return all_main_cat_counts


def restart_pointer(f):
    f.seek(0)
    next(f)
