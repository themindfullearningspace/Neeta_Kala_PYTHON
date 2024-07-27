# without using the pre-defined function
def leap_year_or_not(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

year = int(input("Enter the year: "))
print(f"{year} is a leap year: {leap_year_or_not(year)}")


#Using pre-defined function..'isleap()'
import calendar
def is_leap_year(year):
    return calendar.isleap(year)

year = 2024
print(f"{year} is a leap year: {is_leap_year(year)}")
