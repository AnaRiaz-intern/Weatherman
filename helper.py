class Weather_man ():
    def __init__(self, date, highest_temp, lowest_temp, humidity):
        self.date = date
        self.highest_temp = int(highest_temp) if highest_temp else 0
        self.lowest_temp = int(lowest_temp) if lowest_temp else 0
        self.humidity = int(humidity) if humidity else 0

    def get_date(self):
        return self.date

    def get_highest_temp(self):
        return self.highest_temp

    def get_lowest_temp(self):
        return self.lowest_temp

    def get_humidity(self):        
        return self.humidity

    def __str__(self):
        return f"Date: {self.date}, Highest Temp: {self.highest_temp},Lowest Temp: {self.lowest_temp}, Humidity: {self.humidity}"


# function to read files , deals with NULLs, empty columns as well
def read_file(path):
    data = []
    with open(path, 'r') as file:
        first_line = file.readline().strip().split(',')
        if len(first_line) < 8:  # Check if the first line has enough values
            file.readline()
        for line in file:
            data_values = line.strip().split(',')
            if len(data_values) < 8:  # Check if the line has enough values
                continue
            date = data_values[0]
            highest_temp = data_values[1]
            lowest_temp = data_values[3]
            humidity = data_values[7]

            # Handle missing values by setting them to 0
            highest_temp = int(highest_temp) if highest_temp.strip() else 0
            lowest_temp = int(lowest_temp) if lowest_temp.strip() else 0
            humidity = int(humidity) if humidity.strip() else 0

            required_entry = Weather_man(date, highest_temp, lowest_temp, humidity)
            data.append(required_entry)

    return data

# computes highest temp, lowest temp, highest humidity along years alone
def Yearly_Computations(data):
    if not data:
        print("No data available for this year :(\n")
    highest_temp = 0
    lowest_temp = 0
    high_humidity = 0
    date1 = None
    date2 = None
    date3 = None
    # For each entry,retrieve three values: temp1, temp2, and temp3, 
    # which represent the highest temperature, lowest temperature, and 
    # humidity, respectively, for that particular entry.
    for entry in data:
        temp1 = entry.get_highest_temp()
        temp2 = entry.get_lowest_temp()
        temp3 = entry.get_humidity()
        if (highest_temp == 0) or (temp1 > highest_temp):
            highest_temp = temp1
            date1 = entry.get_date()
        if (lowest_temp == 0) or (temp2 < lowest_temp):
            lowest_temp = temp2
            date2 = entry.get_date()
        if (high_humidity == 0) or (temp3 > high_humidity):
            high_humidity = temp3
            date3 = entry.get_date()
    return highest_temp, date1, lowest_temp, date2, high_humidity, date3


"""
yearly_stats() computes and prints the yearly statistics for a collection of
data rows representing different years. It uses the Yearly_Computations(data)
function to process each individual year's data and then aggregates the results
to find the overall highest temperature, lowest temperature, and highest
humidity among all the years
"""


def yearly_stats(rows):
    highest_temperature = 0
    lowest_temp = 0
    high_humidity = 0
    highest_temperature_day = None
    lowest_temp_day = None
    high_humidity_day = None
    for row in rows:
        current_ht, current_d, curr_lt, curr_lt_d, curr_hh, curr_hh_d = Yearly_Computations(row)
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
    print("Here's Your Yearly Report")
    print("--------------------------------\n")
    print(f"Highest Temp: {highest_temperature} on {highest_temperature_day}")
    print(f"Lowest Temp: {lowest_temp} on {lowest_temp_day}")
    print(f"Highest Humidity: {high_humidity} on {high_humidity_day}")
    print("--------------------------------\n")
    print("\n\n")


# calculates average high temp, low temp, and high humidity
def Monthly_Averages_Findings(data):
    if not data:
        print("No data available for this month :(\n")
        return

    count = len(data)
    total_highest_temp = sum(entry.get_highest_temp() for entry in data)
    total_lowest_temp = sum(entry.get_lowest_temp() for entry in data)
    total_humidity = sum(entry.get_get_humidity() for entry in data)

    average_highest_temp = total_highest_temp / count
    average_lowest_temp = total_lowest_temp / count
    average_humidity = total_humidity / count
    print(f"Average Highest Temperature: {average_highest_temp:.2f}")
    print(f"Average Lowest Temperature: {average_lowest_temp:.2f}")
    print(f"Average Humidity: {average_humidity:.2f}")
    print("----------------------------\n")

# for a given year_month rturns the highest temp in that year+month
def Find_High_temp(data):
    if not data:
        print("No data available :(\n")
    highest_temp = 0
    # min temp on the day with highest temp
    min_temp_on_hottest_day = 0
    # max temp on the coldest day
    high_temp_day = None
    for entry in data:
        temp = entry.get_highest_temp()
        if (highest_temp == 0) or (temp > highest_temp):
            highest_temp = temp
            high_temp_day = entry.get_date()
            min_temp_on_hottest_day = entry.get_lowest_temp()
    return high_temp_day, highest_temp, min_temp_on_hottest_day

# for a given year+month finds lowest temp
def Find_Low_temp(data):
    if not data:
        print("No data available :(\n")
    lowest_temp = 0
    low_temp_day = None
    max_temp_on_coldest_day = 0
    for entry in data:
        temp = entry.get_lowest_temp()
        if (lowest_temp == 0) or (temp < lowest_temp):
            lowest_temp = temp
            low_temp_day = entry.get_date()
            max_temp_on_coldest_day = entry.get_highest_temp()
    return low_temp_day, lowest_temp, max_temp_on_coldest_day

# draws a simple bar chart for monthlu findings


def print_horizontal_bar_chart(case, value, color_code):
    if case == "-c":
        for i in range(int(value)):
            print(color_code + " +", end='')
        print()
    if case == "-d":
        for i in range(int(value)):
            print(color_code + " +", end='')
        print(end='')


# proper way to draw the graphs


def high_low_Graphs(case, rows):
    high_temp = 0
    high_temp_day = None
    min_on_hday = 0
    low_temp = 0
    low_temp_day = None
    max_on_lday = 0
    for row in rows:
        curr_h_day, curr_h_temp, curr_min_on_h_day = Find_High_temp(row)
        if int(curr_h_temp) > int(high_temp) or high_temp == 0:
            high_temp = curr_h_temp
            high_temp_day = curr_h_day
            min_on_hday = curr_min_on_h_day
    print(" Day: ", high_temp_day) 
    print(" Highest Temp: ", high_temp) 
    print(" Min Temp on this day: ", min_on_hday)
    print_horizontal_bar_chart(case, high_temp, "\033[0;31;40m")
    print_horizontal_bar_chart(case, min_on_hday, "\033[0;34;40m")
    print("\033[0;37;40m")
    for row in rows:
        curr_l_day, curr_l_temp, curr_max_on_l_day = Find_Low_temp(row)
        if int(curr_l_temp) < int(low_temp) or low_temp == 0:
            low_temp = curr_l_temp
            low_temp_day = curr_l_day
            max_on_lday = curr_max_on_l_day
    print("\033[0;37;40m", "Day: ", low_temp_day) 
    print(" Lowest Temp: ", low_temp) 
    print(" Min Temp on this day: ", max_on_lday)
    print_horizontal_bar_chart(case, max_on_lday, "\033[0;31;40m")
    print_horizontal_bar_chart(case, low_temp, "\033[0;34;40m")
    print("\033[0;37;40m")
