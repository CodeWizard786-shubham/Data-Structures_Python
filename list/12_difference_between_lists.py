'''
@Author: shubham shirke
@Date: 2023-06-09 17:46:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 17:46:30
@Title : Python program to generate difference between two list.
'''

def difference_in_list(list_elements_1,list_elements_2):
    """
    Description : 
                This function finds the difference between two sets and the stores in the list again.
    Parameters : 
                list_elements_1 : list 1 with integer elements.
                list_elements_2 : list 2 with integer elements.
    Returns      :
                difference_of_list : list with elements of list 1 that are not present in list 2.

    """
    # convert lists to set to perform subtraction
    difference_of_list = list(set(list_elements_1) - set(list_elements_2)) 
    return difference_of_list

# main
def main():
    list_elements_1 = list(map(int, input("Enter numbers separated by spaces: ").split()))
    list_elements_2 = list(map(int, input("Enter numbers separated by spaces: ").split()))
    difference_of_list = difference_in_list(list_elements_1,list_elements_2)
    print(f"The list with the difference between two list is : {difference_of_list}")


if __name__ == "__main__":
    main()