'''
@Author: shubham shirke
@Date: 2023-06-07  10:40:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 10:40:30
@Title : Python program to print number of days between two dates.
'''

from datetime import date

def diff_between_dates(start_date,end_date):
    """
    Description : This function calculates the difference between two dates interms of days.
    Parameters : 
        start_date : start date input from the user. 
        end_date   : end date input from the user.

    Result : The difference in days
    """
    year_1, month_1, day_1 = map(int, start_date.split("-"))   
    year_2, month_2, day_2 = map(int, end_date.split("-"))

    # date format using date function
    date_1 = date(year_1,month_1,day_1)
    date_2 = date(year_2,month_2,day_2)

    difference = abs(date_1 - date_2)

    print(f"The difference in number of days are: {difference.days}")  # date.days function only print days.
    


def main():
    start_date =input("Enter start date in the format (YYYY-MM-DD): ")
    end_date =input("Enter end date in the format (YYYY-MM-DD): ")
    diff_between_dates(start_date,end_date)

if __name__ == "__main__":
    main()