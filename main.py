import helper
import Calander
import os
import sys


# input command line -> python -e 2002 /path/to/filesFolder
n = len(sys.argv)
print("Total arguments passed:", n)
current_path = os.getcwd()
problem_type = sys.argv[1]
folder_name = sys.argv[3]
folder_path = os.path.join(current_path, folder_name)

print("\nYou selected this folder: ", folder_name, "\n")
text_files = []
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        text_files.append(os.path.join(folder_path, filename))

rows = []
if problem_type == "-e":
    given_year = str(sys.argv[2])
    for file_name in text_files:
        if given_year in file_name:
            # store the data of filenames having that year in their
            # title in a separate list "rows"
            rows.append(helper.read_file(file_name))
    # we now have the desired rows
    highest_temperature = 0
    lowest_temp = 0
    high_humidity = 0
    highest_temperature_day = None
    lowest_temp_day = None
    high_humidity_day = None
    for row in rows:
        current_ht, current_d, curr_lt, curr_lt_d, curr_hh, curr_hh_d = helper.Yearly_findings(row)
        if int(current_ht) > int(highest_temperature):
            highest_temperature = current_ht
            highest_temperature_day = current_d
        if int(curr_lt) < int(lowest_temp):
            lowest_temp = curr_lt
            lowest_temp_day = curr_lt_d
        if int(curr_hh) > int(high_humidity):
            high_humidity = curr_hh
            high_humidity_day = curr_hh_d
    print("--------------------------------")
    print("Here's Your yearly Report")
    print("--------------------------------\n")
    print(f"Highest Temp: {highest_temperature} on {highest_temperature_day}")
    print(f"Lowest Temp: {lowest_temp} on {lowest_temp_day}")
    print(f"Highest Humidity: {high_humidity} on {high_humidity_day}")

    print("--------------------------------\n")
    print("\n\n")

if problem_type == "-a":
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

if problem_type == "-c":
    given_year, given_month = Calander.extract_month_and_year(sys.argv[2])
    for file_name in text_files:
        if given_month in file_name and given_year in file_name:
            rows.append(helper.read_file(file_name))


