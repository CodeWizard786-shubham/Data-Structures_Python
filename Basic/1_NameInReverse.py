'''
@Author: shubham shirke
@Date: 2023-06-06  20:23:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-06 20:23:30
@Title : Python program to print name in reverse order having space between characters.
'''


def name_in_reverse(first_name , last_name):
    """
    Description : This function reverse a name with a space input from the user using join and reversed function.
    Parameters : 
        first_name : first name of the user.
        last_name  : last name of the user.
    Result    :  full name of the user in reverse order. 
    """
    full_name = " ".join(reversed([first_name, last_name]))   
  
    print(full_name)
    

# main 
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    name_in_reverse(first_name,last_name)


if __name__ == "__main__":
    main()