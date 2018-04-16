import operator

from common_functions import get_csv_reader, each_funded_project


def run(f):
    main_categories_successful_projects_count = {}
    reader = get_csv_reader(f)

    def add_count_to_main_category(row):
        main_category = row[3]
        main_categories_successful_projects_count.setdefault(main_category, 0)
        main_categories_successful_projects_count[main_category] += 1

    each_funded_project(reader, add_count_to_main_category)

    best_main_category = max(main_categories_successful_projects_count.items(), key=operator.itemgetter(1))[0]
    print(best_main_category)
    return best_main_category
