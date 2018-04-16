import operator

from common_functions import get_csv_reader


def run(f, best_main_category):
    categories_successful_projects_count = {}
    reader = get_csv_reader(f)
    best_main_category

    for row in reader:
        main_category = row[3]
        category = row[2]
        if main_category == best_main_category:
            categories_successful_projects_count.setdefault(category, 0)
            categories_successful_projects_count[category] += 1

    if categories_successful_projects_count != {}:
        category_most_successful = max(categories_successful_projects_count.items(), key=operator.itemgetter(1))[0]
        print(category_most_successful)
    else:
        print("nothing")
