import question1
import question2
import question3
import question4
import question5
from file_handler import download_csv_sheet


def run():
    csv_sheet_name = 'data.csv'
    url = 'https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv'
    download_csv_sheet(csv_sheet_name, url)
    with open(csv_sheet_name, encoding='utf-8') as f:
        print_question_separator('1. What main-category of project has the highest success rate?')
        

        print_question_separator('2. For the main-category of project with highest success rate (question above), what is the category with the highest number of project proposals?')
        

        print_question_separator('3. What is the median pledged amount (usd_pledged_real) of successfully funded projects?')
        

        print_question_separator('4. What is the number of successfully funded projects with more than 5.000$ pledged (usd_pledged_real) per category? (OPTIONAL: In case you decide to visualize all successful projects per category and you perceive any clusters in theresults, try to use the MeanShift algorithm on to see if your gut feeling was correct')
        

        print_question_separator('5. For the main-category with the most successfully funded projects (quantity, not rate of success), what is the goal-amount range (usd_goal_real), e.g. range 0-10k$ , 5-15k$, 100k$-110k$, that contains the most successfully fundedprojects (in quantity, not rate of success)?')
        


def print_question_separator(question_number):
    print('\nQuestion ' + str(question_number), end='\n' + 100 * '-' + '\n')


run()
# It is really bugging me that you have to define function before you call it, so I wrapped everything in run()
# Thanks to that I can order functions as they are called, so you can read code from top to bottom
