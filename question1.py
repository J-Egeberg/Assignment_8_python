import operator

from common_functions import get_csv_reader


def run(f):
    main_categories_successful_projects_count = {}
    reader = get_csv_reader(f)
    for row in reader:
        goal = row[6]
        pleged = row[8]
        if goal <= pleged:
            main_category = row[3]
            main_categories_successful_projects_count.setdefault(main_category, 0)
            main_categories_successful_projects_count[main_category] += 1

    best_main_category = max(main_categories_successful_projects_count.items(), key=operator.itemgetter(1))[0]
    print(best_main_category)
    return best_main_category
