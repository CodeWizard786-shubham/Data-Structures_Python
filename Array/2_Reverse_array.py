'''
@Author: shubham shirke
@Date: 2023-06-08 13:00:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 13:30:30
@Title : Python program to reverse the order of the items in the array.
'''

from array import *
def reverse_array():
    """
    Description : 
            This function creates a array of integers are reverses the array using slicing.
    Parameters :
            none
    Return  : 
            nothing
            prints array in reverse order.
    """
    array_of_integers = array('i', [10,20,30,40,50])
    reverse_array = array_of_integers[::-1]
    
    # print elements in order.
    for i in reverse_array:
        print(i)

# main
def main():
    reverse_array()


if __name__ == "__main__":
    main()