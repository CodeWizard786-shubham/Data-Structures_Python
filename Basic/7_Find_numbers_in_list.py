'''
@Author: shubham shirke
@Date: 2023-06-07  12:15:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 15:15:30
@Title : Python program to find numbers in a list.
'''

def find_in_list(num):
    """
    Description : 
            This function checks if the number taken from the user in present in the list or not.
    Paramenters :
            num : input from the user in int type.
    Result : 
            returns true if num present otherwise false. 
    """
    list = [1, 5, 8, 3]
    for i in list:
        if i == num:
            return True
    return False


def print_result(is_present):   
    """
    Description : 
            This function print present or absent depending on the value pass as parameter.
    Parameters :
            is_presnt : This value is the returned value from find_in_list().
    Result  :
            prints present if number found else print not present.
    """     
    if is_present:
        print("Present")
    else:
        print("Not present")

# main
def main():
    num = int(input("Enter number to find in list: "))
    is_present = find_in_list(num)
    print_result(is_present)


if __name__ == "__main__":
    main()
