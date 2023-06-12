'''
@Author: shubham shirke
@Date: 2023-06-09 23:05:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 23:05:30
@Title : Python program to check whether an element exists within a tuple..
'''


def check_item_in_tuple(tuple_of_elements,element):
    """
    Description : 
            This function iterates over the tuple and checks if the user input matches with any item in tuple.
    Parameters : 
            list_elements : list of elements by user input.
            element : value to check in the tuple of existence.
    Returns : 
            boolean value
    """
    for items in tuple_of_elements:
        if items == element:
            return True

    return False

# main
def main():
    tuple_of_elements = tuple(input("Enter elements separated by spaces: ").split())
    element =input("Enter element to check in tuple: ")
    Output = check_item_in_tuple(tuple_of_elements,element)
    print(f"Output: {Output} ")


if __name__ == "__main__":
    main()
