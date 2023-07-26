import helper
import os
import sys


# input command line -> python -e 2002 /path/to/filesFolder
n = len(sys.argv)
print("Total arguments passed:", n)
current_path = os.getcwd()
problem_type = sys.argv[1]
given_year = str(sys.argv[2])
folder_name = sys.argv[3]
folder_path = os.path.join(current_path, folder_name)
print("\nYou selected this folder: ", folder_name, "\n")
text_files = []
rows = []

if problem_type == "-e":
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            text_files.append(os.path.join(folder_path, filename))
    for file_name in text_files:
        if given_year in file_name:
            # store the data of filenames having that year in their
            # title in a separate list "rows"
            rows.append(helper.read_file(file_name))
    # we now have the desired rows
    highest_temperature = 0
    highest_temperature_day = None
    for row in rows:
        current_ht, current_d = helper.find_highest_temperature_and_day(row)
        if int(current_ht) > int(highest_temperature):
            highest_temperature = current_ht
            highest_temperature_day = current_d

    print(f"Highest Temp: {highest_temperature} on {highest_temperature_day}")
    print("\n\n")
