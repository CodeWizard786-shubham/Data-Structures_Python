'''
@Author: shubham shirke
@Date: 2023-06-09 22:17:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 22:17:30
@Title : Python program to create the colon of a tuple.
'''
from copy import deepcopy

def get_colon_of_tuple(tuple_elements):
    """
    Description : 
            This function creates a subtuple using slicing technique by using colon to specify start and end index.
    Parameters : 
            list_elements : list of elements by user input.
    Returns : 
            sub_tuple : tuple of original tuple.
    """
    tuplex_colon = deepcopy(tuple_elements)
    tuplex_colon[2].append(50)

    return tuplex_colon


# main
def main():
    tuple_elements = ("HELLO", 5, [], True) 
    new_tuple = get_colon_of_tuple(tuple_elements)
    print(f"The new-tuple colon of tuple is: {new_tuple}")


if __name__ == "__main__":
    main()
