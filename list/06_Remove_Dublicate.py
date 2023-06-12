'''
@Author: shubham shirke
@Date: 2023-06-09 14:06:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 14:06:30
@Title :  Python program to remove dublicates from list.
'''


def remove_dublicates(elements_of_list):
    """
    Description : 
            This function creates a list of elements by user string inputs and prints unique values.
    Parameters : 
            elements_of_list : input string of elements from user.
    Returns :
            unique_list    
    """
    elements = elements_of_list.split(" ")
    unique_list = []
    for ele in elements:
        if ele not in unique_list :
            unique_list.append(ele)
    
    return unique_list
        


def main():
    elements_of_list = input("Enter elements for the list(use space): ")
    unique_list = remove_dublicates(elements_of_list)
    print(f"The list after removing dublicates is: {unique_list}")




if __name__ == "__main__":
    main()