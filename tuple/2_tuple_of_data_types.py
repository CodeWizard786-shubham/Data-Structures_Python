'''
@Author: shubham shirke
@Date: 2023-06-09 21:43:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 21:43:30
@Title : python program to create a tuple with different data types0.
'''


def create_tuple(list_elements):
    """
    Description : 
            This function creates a tuple of different data types.
    Parameters : 
            list_elements : list of elements by user input.
    Returns : 
            tuple_of_elements : tuple of list elements of different data type.
    """
    tuple_of_elements = tuple(list_elements)
    return tuple_of_elements


# main
def main():
    list_elements = [1,2.3,'hello','world',3,6+3j]
    tuple_of_list= create_tuple(list_elements)
    print(f"The tuple of elements is : {tuple_of_list}") 


if __name__ == "__main__":
    main()
