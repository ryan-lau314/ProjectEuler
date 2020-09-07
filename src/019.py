def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    month = 1
    year = 1900
    day_of_week = 1
    sunday_counter = 0

    while year <= 2000:
        if day_of_week == 0 and year >= 1901:
            sunday_counter += 1

        if month in [1, 3, 5, 7, 8, 10, 12]:
            day_of_week = (day_of_week + 31) % 7
        elif month in [4, 6, 9, 11]:
            day_of_week = (day_of_week + 30) % 7
        elif is_leap_year(year):
            day_of_week = (day_of_week + 29) % 7

        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    print(sunday_counter)
