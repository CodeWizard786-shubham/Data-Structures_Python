'''
@Author: shubham shirke
@Date: 2023-06-09 21:25:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 21:25:30
@Title : Python program to remove an item from a tuple.
'''


def remove_from_tuple(tuple_of_elements,element):
    """
    Description : 
            This function iterates over the tuple and excludes the elemetn to remove to store in new tuple.
    Parameters : 
            list_elements : list of elements by user input.
            element : element to remove.
    Returns : 
            new_tuple : tuple of elements excluding the element specified by user.
    """
    new_tuple = tuple(item for item in tuple_of_elements if item != element) # tuple comprehension
    return new_tuple


def main():
    tuple_of_elements = tuple(input("Enter elements separated by spaces: ").split())
    element = input("Enter element to remove: ")
    tuple_of_list= remove_from_tuple(tuple_of_elements,element)
    print(f"The tuple of elements is : {tuple_of_list}") 


if __name__ == "__main__":
    main()