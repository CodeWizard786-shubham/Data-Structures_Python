'''
@Author: shubham shirke
@Date: 2023-06-09 21:25:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 21:25:30
@Title : python program to create a tuple.
'''


def create_tuple(list_elements):
    """
    Description : 
            This function converts a list to form a tuple using tuple().
    Parameters : 
            list_elements : list of elements by user input.
    Returns : 
            tuple_of_elements : tuple of list elements.
    """
    tuple_of_elements = tuple(list_elements)
    return tuple_of_elements


def main():
    list_elements = list(map(int, input("Enter elements separated by spaces: ").split()))
    tuple_of_list= create_tuple(list_elements)
    print(f"The tuple of elements is : {tuple_of_list}") 


if __name__ == "__main__":
    main()