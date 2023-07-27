import calendar


def get_month_name(month_number):
    if 1 <= int(month_number) <= 12:
        return calendar.month_name[month_number]
    else:
        return "Invalid month number"


# extracting the month
def extract_month_and_year(a):
    given_year_and_month = str(a)
    split_month_year = given_year_and_month.split('/')
    year_name = split_month_year[0]
    month_number = int(split_month_year[1]) 
    month_name = get_month_name(month_number)
    month_name_shotform = month_name[:3]
    return year_name, month_name_shotform