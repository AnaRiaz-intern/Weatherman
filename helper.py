class Weather_man ():
    def __init__(self, date, highest_temp, lowest_temp, humidity):
        self.date = date
        self.highest_temp = highest_temp
        self.lowest_temp = lowest_temp
        self.humidity = humidity

    def get_date(self):
        return self.date

    def get_highest_temp(self):
        return self.highest_temp

    def get_lowest_temp(self):
        return self.lowest_temp

    def get_get_humidity(self):        
        return self.humidity

    def __str__(self):
        return f"Date: {self.date}, Highest Temp: {self.highest_temp},Lowest Temp: {self.lowest_temp}, Humidity: {self.humidity}"


def read_file(path):
    data = []
    with open(path, 'r') as file:
        file.readline().strip().split(',')
        for line in file:
            data_values = line.strip().split(',')
            # date -> 0th index
            # highest temp -> 1st index
            # lowest temp -> 3rd inex
            # most humid day -> day with max humity -> 7th index
            required_entry = Weather_man(data_values[0], data_values[1],
                                         data_values[3], data_values[7])
            data.append(required_entry)
    return data


def find_highest_temperature_and_day(data):
    if not data:
        print("No data available for this year :(\n")
    highest_temp = 0
    date = None
    for entry in data:
        temp = entry.get_highest_temp()
        if (highest_temp == 0) or (temp > highest_temp):
            highest_temp = temp
            date = entry.get_date()
    return highest_temp, date
