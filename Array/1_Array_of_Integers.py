'''
@Author: shubham shirke
@Date: 2023-06-08 12:40:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 12:40:30
@Title : Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
'''

from array import *

def array_of_integers():
    """
    Description : 
            This function creates a array of five elements and print the elements using their index number.
    Parameters : 
            none
    Retrun    :
            retruns nothing
            print elemnents at that given index.
    """
    array1 = array('i', [10,20,30,40,50])   # array index start from 0 to n-1
    print(array1[0])
    print(array1[1])
    print(array1[2])
    print(array1[3])
    print(array1[4])

# main
def main():
    array_of_integers()


if __name__ == "__main__":
    main()