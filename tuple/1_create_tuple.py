'''
@Author: shubham shirke
@Date: 2023-06-09 21:25:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 21:25:30
@Title : python program to create a tuple.
'''


def create_tuple():
    """
    Description : 
            This function creates a tuple of comma seperated elements enclosed in open and close paranthesis.
    Parameters : 
            list_elements : list of elements by user input.
    Returns : 
            tuple_of_elements : tuple of list elements.
    """
    tuple_of_elements = (1,2,3,4,5,6)
    return tuple_of_elements



def main():
    tuple_of_list= create_tuple()
    print(f"The tuple of elements is : {tuple_of_list}") 


if __name__ == "__main__":
    main()