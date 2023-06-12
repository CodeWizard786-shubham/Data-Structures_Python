'''
@Author: shubham shirke
@Date: 2023-06-09 19:02:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 19:02:30
@Title : Python program to split a list based on first character of word.
'''

from itertools import groupby
from operator import itemgetter


def split_list(list_elements): 
    """
    Description : 
            This function finds the first char of every word and group them together.
    Parameters : 
            list_elements : list of elements
    Returns :
            none
            prints letter and words.
    """
 
    for letter, words in groupby(sorted(list_elements), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(" ",word)
        print("")


# main
def main():
    list_elements = ["cat","dog","cow","tiger","lion","Fox","Shark","Snake","turtle","mouse","monkey","bear"]
    result = split_list(list_elements)
    print(f"list based on first character is: {result}")


if __name__ == "__main__":
    main()