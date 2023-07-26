from colorama import Fore, init
init()


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


# def read_file(path):
#     data = []
#     with open(path, 'r') as file:
#         first_line = file.readline().strip().split(',')
#         if not first_line:
#             file.readline()
#         for line in file:
#             data_values = line.strip().split(',')
#             # date -> 0th index
#             # highest temp -> 1st index
#             # lowest temp -> 3rd inex
#             # most humid day -> day with max humity -> 7th index
#             required_entry = Weather_man(data_values[0], data_values[1],
#                                          data_values[3], data_values[7])
#             data.append(required_entry)
#     return data
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


def Yearly_findings(data):
    if not data:
        print("No data available for this year :(\n")
    highest_temp = 0
    lowest_temp = 0
    high_humidity = 0
    date1 = None
    date2 = None
    date3 = None
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


# Function to draw the bar chart


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


def Find_Low_temp(data):
    if not data:
        print("No data available :(\n")
    lowest_temp = 0
    # max temp on the coldest day
    max_temp_on_coldest_day = 0
    low_temp_day = None
    for entry in data:
        temp = entry.get_lowest_temp()
        if (lowest_temp == 0) or (temp < lowest_temp):
            lowest_temp = temp
            low_temp_day = entry.get_date()
            max_temp_on_coldest_day = entry.get_highest_temp()
    return low_temp_day, lowest_temp, max_temp_on_coldest_day


def print_horizontal_bar_chart(value, color_code):
    for i in range(int(value)):
        print(color_code + " +", end='')
    print()