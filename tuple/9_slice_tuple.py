'''
@Author: shubham shirke
@Date: 2023-06-09 22:34:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 22:34:30
@Title : Python program to slice a tuple.
'''


def get_slice_of_tuple(tuple_of_elements):
    """
    Description : 
            This function creates a subtuple using slicing technique by using colon to specify start and end index.
    Parameters : 
            list_elements : list of elements by user input.
    Returns : 
            sub_tuple : slice of original tuple.
    """
    sub_tuple = tuple_of_elements[0:3]  # use of colon through slicing technique
    return sub_tuple


# main
def main():
    tuple_of_elements = tuple(input("Enter elements separated by spaces: ").split())
    sub_tuple = get_slice_of_tuple(tuple_of_elements)
    print(f"The slice of the tuple is: {sub_tuple}")


if __name__ == "__main__":
    main()
