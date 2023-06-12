'''
@Author: shubham shirke
@Date: 2023-06-08 14:22:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 14:22:30
@Title : Python program to remove the first occurrence of a specified element from an array.
'''

from array import *

def remove_occurance():
    """
    Description : 
            This function finds the element in the array and if found removes its first occurance from array.
    Parameters : 
            none
    Return     :
            returns array_1
    """
    array_1 = array('i',[1,2,3,4,1,3,4,5,1])
    element = 2
    if element in array_1:
        array_1.remove(element)
    
    return array_1

# main
def main():
    new_array = remove_occurance()
    print(f"New array is: {new_array}")


if __name__ == "__main__":
    main()