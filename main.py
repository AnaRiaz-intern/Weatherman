import helper
import Calander
import os
import sys


# input command line -> python -e 2002 /path/to/filesFolder
n = len(sys.argv)
print("Total arguments passed:", n)
current_path = os.getcwd()
case = sys.argv[1]
folder_name = sys.argv[3]
folder_path = os.path.join(current_path, folder_name)

print("\nYou selected this folder: ", folder_name, "\n")
text_files = []
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        text_files.append(os.path.join(folder_path, filename))

rows = []

#####################################################################
#########################     case 1    #############################
#####################################################################
if case == "-e":
    given_year = str(sys.argv[2])
    for file_name in text_files:
        if given_year in file_name:
            # store the data of filenames having that year in their
            # title in a separate list "rows"
            rows.append(helper.read_file(file_name))
    helper.yearly_stats(rows)

#####################################################################
#########################     case 2    #############################
#####################################################################

if case == "-a":
    given_year, given_month = Calander.extract_month_and_year(sys.argv[2])
    print("\n---------------------------------")
    print("Here's Your Monthly Report")
    print("---------------------------------")
    print("Year:", given_year, " | Month:", given_month, "\n")
    for file_name in text_files:
        if given_month in file_name:
            if given_year in file_name:
                rows.append(helper.read_file(file_name))
    for row in rows:
        helper.Monthly_Findings(row)

#####################################################################
#########################     case 3    #############################
#####################################################################

if case == "-c":
    given_year, given_month = Calander.extract_month_and_year(sys.argv[2])
    for file_name in text_files:
        if given_month in file_name and given_year in file_name:
            rows.append(helper.read_file(file_name))
    helper.high_low_Graphs(case, rows)

#####################################################################
#########################     case 3    #############################
#####################################################################


if case == "-d":
    given_year, given_month = Calander.extract_month_and_year(sys.argv[2])
    for file_name in text_files:
        if given_month in file_name and given_year in file_name:
            rows.append(helper.read_file(file_name))
    helper.high_low_Graphs(case, rows)