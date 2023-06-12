'''
@Author: shubham shirke
@Date: 2023-06-09 14:45:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 14:45:30
@Title :  Python program to copy or clone a list.
'''


def copy_list(elements_of_list):
    """
    Description : 
            This function stores elements in the original_list and using copy function of list creates a new clone_list.
    Parameters : 
            elements_of_list : string of elements from user.
    Return  :
            original_list
            clone_list
    """
    elements = elements_of_list.split(" ")   
    original_list = []
    clone_list = []
    # store elements in list.
    for ele in elements:
        original_list.append(ele)

    clone_list = original_list.copy()   # copy function in list

    return original_list,clone_list


# main
def main():
    elements_of_list = input("Enter elemetents for list: ")
    original_list , clone_list = copy_list(elements_of_list)
    print(f"The original list is: {original_list}")
    print(f"The clone list is: {clone_list}")


if __name__ == "__main__":
    main()