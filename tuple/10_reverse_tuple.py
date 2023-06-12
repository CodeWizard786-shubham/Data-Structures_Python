'''
@Author: shubham shirke
@Date: 2023-06-09 22:36:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 22:36:30
@Title : Python program to reverse a tuple.
'''


def get_reverse_of_tuple(tuple_of_elements):
    """
    Description : 
            This function reverse the elements in the tuple by printing from last element using slicing.
    Parameters : 
            list_elements : list of elements by user input.
    Returns : 
            reverse_tuple : reverse of original tuple.
    """
    reverse_tuple = tuple_of_elements[::-1]  # use of slicing to print in reverse order
    return reverse_tuple


# main
def main():
    tuple_of_elements = tuple(input("Enter elements separated by spaces: ").split())
    reverse_tuple = get_reverse_of_tuple(tuple_of_elements)
    print(f"The reverse of the tuple is: {reverse_tuple}")


if __name__ == "__main__":
    main()
