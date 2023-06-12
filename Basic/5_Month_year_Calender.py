'''
@Author: shubham shirke
@Date: 2023-06-07  10:20:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 10:20:30
@Title : Python program to print calender for a given month and year.
'''

import calendar


def print_calender(month,year):
    """
    Description : This function prints calender for given month and year.
    Parameters : 
        month - month number
        year - 4 digit year
    Result :  displays calender. 
    """
    if len(str(year)) != 4:
        print("Enter enter 4 digit year number")
    else : 
        print()
        print(calendar.month(year,month))   # calender.month function for display calender for month and year


# main
def main():
    month = int(input("Enter month number: "))
    year = int(input("Enter year: "))
    print_calender(month,year)


if __name__ == "__main__":
    main()

